"""Role-B NRP health check, run from the laptop every working block (no pod needed).
Reproduces the portal's violation tests for our pods from the public Thanos API:
GPU mean over 1 h / 3 h (idle-warning window) / 6 h (admin-deletion window) / 1 d
(Violations page), CPU and RSS 1-day medians against requests.
  python scripts/nrp_status_b.py [--all]   (--all: every pod in the namespace)"""
import json, subprocess, sys, urllib.parse, urllib.request

NS = "ecepxie"
THANOS = "https://thanos.nrp-nautilus.io/api/v1/query"
GRAFANA = f"https://grafana.nrp-nautilus.io/d/dRG9q0Ymz/k8s-compute-resources-namespace-gpus?var-namespace={NS}"


def q(expr):
    url = THANOS + "?" + urllib.parse.urlencode({"query": expr})
    with urllib.request.urlopen(url, timeout=60) as r:
        out = json.load(r)
    return {s["metric"].get("pod", ""): float(s["value"][1]) for s in out["data"]["result"]}


def main():
    sel = 'pod=~".*"' if "--all" in sys.argv else 'pod=~"selrm-b-.*"'
    pods = subprocess.run(["kubectl", "-n", NS, "get", "pods", "-l", "app=selrm-b", "-o", "wide", "--no-headers"],
                          capture_output=True, text=True).stdout.strip()
    print("pods (app=selrm-b):\n" + (pods or "  none"))
    gpu = {w: q(f'avg by (pod)(avg_over_time(DCGM_FI_DEV_GPU_UTIL{{namespace="{NS}",{sel}}}[{w}]))')
           for w in ("1h", "3h", "6h", "1d")}
    req_gpu = q(f'sum by (pod)(kube_pod_container_resource_requests{{namespace="{NS}",{sel},resource=~"nvidia_com_.*"}})')
    cpu = q(f'sum by (pod)(quantile_over_time(0.5, node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate'
            f'{{namespace="{NS}",{sel},container!=""}}[1d]))')
    req_cpu = q(f'sum by (pod)(kube_pod_container_resource_requests{{namespace="{NS}",{sel},resource="cpu"}})')
    rss = q(f'sum by (pod)(quantile_over_time(0.5, container_memory_rss{{namespace="{NS}",{sel},container!=""}}[1d]))')
    req_mem = q(f'sum by (pod)(kube_pod_container_resource_requests{{namespace="{NS}",{sel},resource="memory"}})')
    ns_gpu = q(f'avg_over_time(namespace_gpu_utilization{{namespace="{NS}"}}[1h])')
    print(f"\nnamespace GPU utilisation (1 h mean): {list(ns_gpu.values())[0] if ns_gpu else 'n/a'}   dashboard: {GRAFANA}")
    print(f"\n{'pod':58s} {'gpus':>4s} {'gpu1h':>6s} {'gpu3h':>6s} {'gpu6h':>6s} {'gpu1d':>6s} {'cpu/req':>8s} {'rss/req':>8s} flags")
    for p in sorted(set(req_gpu) | set(req_cpu)):
        g = {w: gpu[w].get(p) for w in gpu}
        c = cpu.get(p, 0) / req_cpu[p] if req_cpu.get(p) else None
        m = rss.get(p, 0) / req_mem[p] if req_mem.get(p) else None
        flags = []
        if req_gpu.get(p) and g["1d"] is not None and g["1d"] < 40:
            flags.append("GPU<40(1d)")
        if req_gpu.get(p) and g["3h"] is not None and g["3h"] < 40:
            flags.append("GPU<40(3h)")
        if req_cpu.get(p, 0) > 1 and c is not None and not 0.2 <= c <= 2.0:
            flags.append("CPU")
        if req_mem.get(p, 0) > 2 * 2**30 and m is not None and not 0.2 <= m <= 1.5:
            flags.append("MEM")
        fmt = lambda v: f"{v:6.1f}" if v is not None else "     -"
        print(f"{p[:58]:58s} {int(req_gpu.get(p, 0)):4d} {fmt(g['1h'])} {fmt(g['3h'])} {fmt(g['6h'])} {fmt(g['1d'])} "
              f"{(f'{c:8.2f}' if c is not None else '       -')} {(f'{m:8.2f}' if m is not None else '       -')} {' '.join(flags)}")
    print("\nPortal Violations page (login): https://nrp.ai/userinfo  | pods younger than 30 min are not judged")


if __name__ == "__main__":
    main()
