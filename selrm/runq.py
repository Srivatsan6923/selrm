"""Run claims, heartbeats and GPU-utilisation logging for B's queue runners
(INTERFACES 7). Owner B. Everything lives under results/<run_id>/ on the shared
PVC: CLAIMED_<role>, HEARTBEAT, DONE, FAILED_<n>, gpu_util.csv."""
from __future__ import annotations

import csv
import os
import subprocess
import threading
import time

ROLE = "B"
STALE_OTHER_S = 3 * 3600      # INTERFACES: a claim with no heartbeat for 3 h may be re-claimed
STALE_OWN_S = 15 * 60         # our runners heartbeat every 2 min; a silent own claim is a dead pod
MAX_FAILS = 2                 # ROLE.md: a run that fails twice is marked failed


def _age(path):
    try:
        return time.time() - os.path.getmtime(path)
    except FileNotFoundError:
        return None


def state(rdir: str) -> str:
    """done | failed | claimed | free (free includes stale claims)."""
    if os.path.exists(f"{rdir}/DONE"):
        return "done"
    if fails(rdir) >= MAX_FAILS:
        return "failed"
    claims = [f for f in os.listdir(rdir) if f.startswith("CLAIMED_")] if os.path.isdir(rdir) else []
    if not claims:
        return "free"
    hb = _age(f"{rdir}/HEARTBEAT")
    if hb is None:
        hb = min(_age(f"{rdir}/{c}") or 0 for c in claims)
    limit = STALE_OWN_S if claims == [f"CLAIMED_{ROLE}"] else STALE_OTHER_S
    return "claimed" if hb < limit else "free"


def fails(rdir: str) -> int:
    return len([f for f in os.listdir(rdir) if f.startswith("FAILED_")]) if os.path.isdir(rdir) else 0


def claim(rdir: str, owner: str, settle_s: float = 2.0) -> bool:
    """Claim by O_EXCL create (CephFS honours it across clients). Stale claims are
    moved aside first; because two runners can race on the same stale claim, the
    claim is re-read after `settle_s` and kept only if it still names `owner`."""
    os.makedirs(rdir, exist_ok=True)
    if state(rdir) != "free":
        return False
    for f in os.listdir(rdir):
        if f.startswith("CLAIMED_"):
            try:
                os.replace(f"{rdir}/{f}", f"{rdir}/stale_{f}")
            except FileNotFoundError:
                return False
    me = f"{owner} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {os.getpid()}\n"
    try:
        fd = os.open(f"{rdir}/CLAIMED_{ROLE}", os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, me.encode())
    os.close(fd)
    time.sleep(settle_s)
    try:
        if open(f"{rdir}/CLAIMED_{ROLE}").read() != me:
            return False
    except FileNotFoundError:
        return False
    beat(rdir)
    return True


def beat(rdir: str):
    with open(f"{rdir}/HEARTBEAT", "w") as f:
        f.write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")


def release(rdir: str, ok: bool, reason: str = ""):
    """ok -> DONE; else FAILED_<n> with the reason, and the claim is dropped so a
    second attempt can start at once."""
    if ok:
        open(f"{rdir}/DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")
    else:
        open(f"{rdir}/FAILED_{fails(rdir) + 1}", "w").write(reason[-4000:] + "\n")
    for f in os.listdir(rdir):
        if f.startswith("CLAIMED_"):
            os.remove(f"{rdir}/{f}")


def gpu_sample():
    """-> (util %, memory MiB) of GPU 0, or None if nvidia-smi fails."""
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu,memory.used",
                              "--format=csv,noheader,nounits"], capture_output=True, text=True,
                             timeout=20).stdout.strip().splitlines()[0]
        u, m = (float(x) for x in out.split(","))
        return u, m
    except Exception:
        return None


def util_stats(utils: list, period_s: int = 30, window_s: int = 300) -> dict:
    """mean, 10th percentile and share of 5-minute windows whose mean is below 40%."""
    if not utils:
        return {"gpu_util_mean": None, "gpu_util_p10": None, "gpu_windows_below40": None, "gpu_samples": 0}
    s = sorted(utils)
    k = max(1, window_s // period_s)
    wins = [utils[i:i + k] for i in range(0, len(utils), k)]
    wins = [w for w in wins if len(w) * 2 >= k] or wins          # drop a short tail window
    below = sum(sum(w) / len(w) < 40 for w in wins)
    return {"gpu_util_mean": round(sum(utils) / len(utils), 1),
            "gpu_util_p10": s[int(0.1 * (len(s) - 1))],
            "gpu_windows_below40": round(below / len(wins), 3), "gpu_samples": len(utils)}


class GpuMonitor(threading.Thread):
    """Samples GPU 0 every `period` s into the current run's gpu_util.csv and a
    job-wide CSV, touches HEARTBEAT, and aborts the process (exit 3) when
    utilisation stays below `floor` % for `patience` s (a hung pod must not sit on
    a GPU). Grace: the first `grace` s after start (imports + weight loading)."""

    def __init__(self, job_csv: str, period=30, floor=5.0, patience=600, grace=900, log=print):
        super().__init__(daemon=True)
        self.job_csv, self.period, self.floor, self.patience, self.grace = job_csv, period, floor, patience, grace
        self.log, self.rdir, self.utils, self.t0, self.low_since = log, None, [], time.time(), None
        self.lock = threading.Lock()

    def start_run(self, rdir: str):
        with self.lock:
            self.rdir, self.utils = rdir, []

    def end_run(self) -> dict:
        with self.lock:
            st, self.rdir, self.utils = util_stats(self.utils, self.period), None, []
        return st

    def run(self):
        while True:
            smp, now = gpu_sample(), time.time()
            ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))
            with self.lock:
                rdir = self.rdir
                if smp is not None:
                    u, m = smp
                    rows = [self.job_csv] + ([f"{rdir}/gpu_util.csv"] if rdir else [])
                    for path in rows:
                        new = not os.path.exists(path)
                        with open(path, "a", newline="") as f:
                            w = csv.writer(f)
                            if new:
                                w.writerow(["time", "utilization.gpu", "memory.used.MiB"])
                            w.writerow([ts, u, m])
                    if rdir:
                        self.utils.append(u)
                    self.low_since = (self.low_since or now) if u < self.floor else None
            if rdir:
                try:
                    beat(rdir)
                except OSError as e:
                    self.log(f"heartbeat failed: {e}")
            if (self.low_since is not None and now - self.low_since >= self.patience
                    and now - self.t0 >= self.grace):
                reason = (f"WATCHDOG: GPU utilisation below {self.floor}% for "
                          f"{int(now - self.low_since)} s; aborting (exit 3)")
                self.log(reason)
                if rdir:
                    try:
                        release(rdir, ok=False, reason=reason)
                    except OSError:
                        pass
                os._exit(3)
            time.sleep(self.period)
