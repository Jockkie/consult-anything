#!/usr/bin/env python3
"""Rank bottleneck candidates from a Consult Anything dossier.

Usage:
    python3 bottleneck.py dossier.json [--hours-per-day 8] [--json]

Reads the `steps` list and prints, per step: capacity per week (the optional
`capacity_per_week`, else `throughput_per_week`; point or range midpoint),
effective capacity after rework, the flow arriving from the step before, queue,
flow efficiency (work time divided by lead time) and flags.

A step is a candidate when work waits in front of it and its effective capacity
is lower than what arrives. Candidates are ranked by the gap (arriving minus
capacity). Steps whose capacity or queue is labelled `unknown` (or missing) are
left out of the ranking: never fill in a number just to make a ranking appear.
The script reports which `inferred` values the ranking relies on.
Standard library only.
"""
import argparse
import json
import sys


def point(field):
    """Return (value, label, is_range) for a {value|low/high, label} field."""
    if not isinstance(field, dict):
        return None, "unknown", False
    label = field.get("label", "unknown")
    if field.get("value") is not None:
        return float(field["value"]), label, False
    low, high = field.get("low"), field.get("high")
    if low is not None and high is not None:
        return (float(low) + float(high)) / 2.0, label, True
    return None, label, False


def analyse(dossier, hours_per_day):
    rows = []
    for step in dossier.get("steps", []):
        cap_field = step.get("capacity_per_week") or step.get("throughput_per_week")
        tp, tp_label, tp_range = point(cap_field)
        queue, q_label, _ = point(step.get("queue"))
        rework, _, _ = point(step.get("rework_pct"))
        lead_days, _, _ = point(step.get("lead_time_days"))
        work_hours, _, _ = point(step.get("work_time_hours"))

        effective = None
        if tp is not None and tp_label != "unknown":
            effective = tp * (1 - (rework or 0) / 100.0)

        flow_eff = None
        if lead_days and work_hours is not None and lead_days > 0:
            flow_eff = min(1.0, work_hours / (lead_days * hours_per_day))

        flags = []
        if queue and queue > 0:
            flags.append("work waiting")
        if flow_eff is not None and flow_eff < 0.15:
            flags.append("mostly waiting (flow efficiency < 15%)")
        if rework and rework >= 10:
            flags.append("high rework (>= 10%)")
        if effective is None:
            flags.append("capacity unknown: not ranked")
        if tp_range:
            flags.append("range estimate")

        rows.append({
            "step": step.get("name", "?"),
            "throughput": tp,
            "throughput_label": tp_label,
            "effective_throughput": effective,
            "queue": queue,
            "queue_label": q_label,
            "flow_efficiency": flow_eff,
            "rework_pct": rework,
            "flags": flags,
        })

    # flow arriving at each step: the first step's own volume, then whatever the
    # previous step can actually pass on
    arriving = None
    for i, r in enumerate(rows):
        if i == 0:
            r["arriving"] = r["throughput"] if r["throughput_label"] != "unknown" else None
            arriving = r["arriving"]
        else:
            r["arriving"] = arriving
        out = r["effective_throughput"]
        if arriving is not None and out is not None:
            arriving = min(arriving, out)
        elif out is not None and i > 0:
            arriving = None  # unknown upstream breaks the chain
        elif i == 0:
            arriving = r["arriving"]
        else:
            arriving = None

    candidates = []
    for i, r in enumerate(rows):
        if i == 0 or r["effective_throughput"] is None or r["queue_label"] == "unknown":
            continue
        waiting = r["queue"] is not None and r["queue"] > 0
        if r["arriving"] is not None and waiting and r["effective_throughput"] < r["arriving"]:
            r["gap"] = r["arriving"] - r["effective_throughput"]
            candidates.append(r)
        elif waiting and r["arriving"] is not None and r["effective_throughput"] >= r["arriving"]:
            r["flags"].append("work waiting but capacity is enough: starved or waiting on the customer, not the constraint")

    if candidates:
        ranked = sorted(candidates, key=lambda r: -r["gap"])
    else:
        # fallback: lowest effective capacity among steps with work waiting
        pool = [r for r in rows if r["effective_throughput"] is not None and r["queue"] and r["queue"] > 0]
        ranked = sorted(pool, key=lambda r: r["effective_throughput"])

    used_inferred = []
    for r in ranked[:2]:
        if r["throughput_label"] == "inferred":
            used_inferred.append(f"{r['step']}.capacity")
        if r["queue_label"] == "inferred":
            used_inferred.append(f"{r['step']}.queue")
    return rows, [c["step"] for c in ranked[:2]], used_inferred, bool(candidates)


def fmt(value, pct=False):
    if value is None:
        return "?"
    if pct:
        return f"{value * 100:.0f}%"
    return f"{value:g}" if float(value).is_integer() else f"{value:.1f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("dossier")
    parser.add_argument("--hours-per-day", type=float, default=8.0,
                        help="working hours per day used for flow efficiency (default 8)")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = parser.parse_args()

    with open(args.dossier, encoding="utf-8") as fh:
        dossier = json.load(fh)

    rows, top, used_inferred, by_gap = analyse(dossier, args.hours_per_day)

    if args.json:
        json.dump({"steps": rows, "top_candidates": top, "inferred_values_used": used_inferred,
                   "method": "gap" if by_gap else "lowest capacity with work waiting"},
                  sys.stdout, indent=2, ensure_ascii=False)
        print()
        return

    print("| Step | Capacity per week | Effective | Arriving | Waiting | Flow efficiency | Rework | Flags |")
    print("|------|-------------------|-----------|----------|---------|-----------------|--------|-------|")
    for r in rows:
        name = f"**{r['step']}**" if top and r["step"] == top[0] else r["step"]
        print(f"| {name} | {fmt(r['throughput'])} ({r['throughput_label']}) | "
              f"{fmt(r['effective_throughput'])} | {fmt(r.get('arriving'))} | {fmt(r['queue'])} | "
              f"{fmt(r['flow_efficiency'], pct=True)} | "
              f"{fmt(r['rework_pct'])}{'%' if r['rework_pct'] is not None else ''} | "
              f"{', '.join(r['flags']) or '-'} |")
    print()
    if top:
        print(f"Prime candidate: {top[0]}" + (f" (runner-up: {top[1]})" if len(top) > 1 else "")
              + ("" if by_gap else " (fallback: lowest capacity with work waiting; demand chain incomplete)"))
        if used_inferred:
            print("Ranking relies on inferred values: " + ", ".join(used_inferred) + ". Confirm or measure them before Gate 2.")
    else:
        print("Not enough numbers to rank candidates. Use range estimates or a measurement week.")
    print(f"Flow efficiency assumes {args.hours_per_day:g} working hours per day.")


if __name__ == "__main__":
    main()
