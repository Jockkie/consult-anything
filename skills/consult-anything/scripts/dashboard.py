#!/usr/bin/env python3
"""Build a one-file HTML dashboard from a Consult Anything dossier.

Usage:
    python3 dashboard.py dossier.json dashboard.html

Shows the goal, the bottleneck, a process map with throughput per step (ranges
as whiskers), queues, the root cause, the baseline and, when follow-ups exist,
before versus after. No external files or scripts; opens in any browser.
Standard library only.
"""
import html
import json
import sys


def point(field):
    if not isinstance(field, dict):
        return None, None, None, "unknown"
    label = field.get("label", "unknown")
    if field.get("value") is not None:
        v = float(field["value"])
        return v, v, v, label
    low, high = field.get("low"), field.get("high")
    if low is not None and high is not None:
        low, high = float(low), float(high)
        return (low + high) / 2, low, high, label
    return None, None, None, label


def esc(value):
    return html.escape("" if value is None else str(value))


def num(value):
    if value is None:
        return "?"
    return f"{value:g}" if float(value).is_integer() else f"{value:.1f}"


def process_svg(steps, bottleneck):
    rows = []
    for s in steps:
        mid, low, high, label = point(s.get("throughput_per_week"))
        queue, _, _, _ = point(s.get("queue"))
        rows.append((s.get("name", "?"), mid, low, high, label, queue))
    known = [r[3] for r in rows if r[3] is not None]
    top = max(known) if known else 1.0
    width, left, right, row_h = 760, 170, 120, 44
    plot_w = width - left - right
    height = 40 + row_h * len(rows)
    x = lambda v: left + (v / top) * plot_w if top else left
    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="Throughput per step per week">']
    parts.append(f'<text x="{left}" y="20" class="axis">units per week</text>')
    for i, (name, mid, low, high, label, queue) in enumerate(rows):
        y = 40 + i * row_h
        is_bn = name == bottleneck
        cls = "bar bn" if is_bn else "bar"
        parts.append(f'<text x="{left - 12}" y="{y + 20}" text-anchor="end" class="{"name bn-text" if is_bn else "name"}">{esc(name)}</text>')
        if mid is None:
            parts.append(f'<text x="{left}" y="{y + 20}" class="muted">unknown</text>')
        else:
            parts.append(f'<rect x="{left}" y="{y + 6}" width="{max(2, x(mid) - left):.1f}" height="20" rx="4" class="{cls}"/>')
            if low != high:
                parts.append(f'<line x1="{x(low):.1f}" x2="{x(high):.1f}" y1="{y + 16}" y2="{y + 16}" class="whisker"/>')
                parts.append(f'<line x1="{x(low):.1f}" x2="{x(low):.1f}" y1="{y + 10}" y2="{y + 22}" class="whisker"/>')
                parts.append(f'<line x1="{x(high):.1f}" x2="{x(high):.1f}" y1="{y + 10}" y2="{y + 22}" class="whisker"/>')
            value_txt = f"{num(low)}–{num(high)}" if low != high else num(mid)
            parts.append(f'<text x="{x(high if high is not None else mid) + 8:.1f}" y="{y + 20}" class="val">{esc(value_txt)} · {esc(label)}</text>')
        if queue:
            parts.append(f'<text x="{width - 8}" y="{y + 20}" text-anchor="end" class="queue">{num(queue)} waiting</text>')
    parts.append("</svg>")
    return "".join(parts)


def metric_table(dossier):
    baseline = dossier.get("baseline", {}) or {}
    follow_ups = [f for f in dossier.get("follow_ups", []) or [] if f.get("metrics")]
    latest = follow_ups[-1] if follow_ups else None
    after = {m.get("metric"): m for m in (latest or {}).get("metrics", [])}
    head = f"<tr><th>Metric</th><th>Baseline {esc(baseline.get('date', ''))}</th>"
    head += f"<th>Follow-up {esc(latest.get('date', ''))}</th></tr>" if latest else "</tr>"
    body = []
    for m in baseline.get("metrics", []) or []:
        row = f"<tr><td>{esc(m.get('metric'))}</td><td>{esc(num(m.get('value')))} <span class='lbl'>{esc(m.get('label', ''))}</span></td>"
        if latest:
            a = after.get(m.get("metric"))
            row += f"<td class='good'>{esc(num(a.get('value'))) if a else '?'}</td>"
        body.append(row + "</tr>")
    if not body:
        return "<p class='muted'>No baseline recorded yet.</p>"
    return f"<table>{head}{''.join(body)}</table>"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as fh:
        d = json.load(fh)

    biz = d.get("business", {}) or {}
    bn = d.get("bottleneck", {}) or {}
    goal = d.get("goal", {}) or {}
    rc = d.get("root_cause", {}) or {}
    sol = d.get("solution", {}) or {}
    tests = [t.get("score") for t in d.get("tests", []) or [] if t.get("score") is not None]
    avg = sum(tests) / len(tests) if tests else None
    chain = "".join(f"<li>{esc(c)}</li>" for c in rc.get("chain", []) or [])

    page = f"""<!doctype html>
<html lang="{esc((d.get('meta') or {}).get('language', 'en'))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Consult Anything · {esc(biz.get('summary', 'Dashboard'))}</title>
<style>
:root {{ --bg:#F5F5DC; --fg:#212121; --muted:#5D4037; --line:rgba(33,33,33,.12); --bar:rgba(33,33,33,.22); --accent:#F57C00; --good:#388E3C; --card:#FBFBEE; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#212121; --fg:#F5F5DC; --muted:rgba(245,245,220,.62); --line:rgba(245,245,220,.12); --bar:rgba(245,245,220,.28); --accent:#F57C00; --good:#C8E6C9; --card:#292929; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:15px/1.55 Inter, system-ui, -apple-system, Segoe UI, sans-serif; font-variant-numeric:tabular-nums; }}
main {{ max-width:880px; margin:0 auto; padding:40px 24px 72px; }}
.eyebrow {{ font-size:11px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-bottom:14px; }}
.eyebrow::before {{ content:""; display:inline-block; width:22px; height:2px; background:var(--accent); vertical-align:middle; margin-right:10px; }}
h1 {{ font-size:30px; font-weight:700; letter-spacing:-0.04em; line-height:1.15; margin:0 0 6px; }}
h2 {{ font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:.14em; color:var(--muted); margin:36px 0 12px; }}
.lead {{ font-family:Spectral, Georgia, serif; font-size:20px; line-height:1.45; margin:18px 0 0; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:18px 20px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; }}
.k {{ color:var(--muted); font-size:12.5px; }}
.v {{ font-size:22px; font-weight:700; letter-spacing:-0.03em; }}
.accent {{ color:var(--accent); }} .good {{ color:var(--good); font-weight:600; }}
svg {{ width:100%; height:auto; font-family:Inter, system-ui, sans-serif; }}
svg .name {{ fill:var(--fg); font-size:13px; }} svg .bn-text {{ fill:var(--accent); font-weight:700; }}
svg .bar {{ fill:var(--bar); }} svg .bar.bn {{ fill:var(--accent); }}
svg .whisker {{ stroke:var(--fg); stroke-width:1.25; }}
svg .val, svg .axis, svg .muted {{ fill:var(--muted); font-size:12px; }}
svg .queue {{ fill:var(--accent); font-size:12px; font-weight:600; }}
table {{ border-collapse:collapse; width:100%; }} th, td {{ text-align:left; padding:9px 10px; border-bottom:1px solid var(--line); }}
th {{ color:var(--muted); font-weight:500; font-size:12.5px; }}
.lbl {{ color:var(--muted); font-size:12px; }} .muted {{ color:var(--muted); }}
.rc {{ font-family:Spectral, Georgia, serif; font-size:17px; }}
ol {{ margin:0; padding-left:22px; }}
footer {{ margin-top:44px; color:var(--muted); font-size:12px; border-top:1px solid var(--line); padding-top:14px; }}
</style>
</head>
<body><main>
<div class="eyebrow">Consult Anything · by Jockkie Studio</div>
<h1>{esc(biz.get('summary', 'Your business'))}</h1>
<div class="muted">Updated {esc((d.get('meta') or {}).get('updated', ''))}</div>
<p class="lead">Bottleneck: <strong class="accent">{esc(bn.get('step', 'not yet confirmed'))}</strong>. {esc(bn.get('evidence', ''))}</p>

<h2>At a glance</h2>
<div class="grid">
  <div class="card"><div class="k">Goal</div><div class="v">{esc(goal.get('target', '?'))}</div><div class="k">{esc(goal.get('metric', ''))} · by {esc(goal.get('date', '?'))}</div></div>
  <div class="card"><div class="k">Bottleneck type</div><div class="v">{esc((bn.get('type') or '?').replace('_', ' '))}</div><div class="k">label: {esc(bn.get('label', 'unknown'))}</div></div>
  <div class="card"><div class="k">Test average</div><div class="v">{esc(f'{avg:.1f}' if avg is not None else '?')} / 10</div><div class="k">{len(tests)} of 10 runs scored</div></div>
  <div class="card"><div class="k">Follow-up</div><div class="v">{esc((d.get('meta') or {}).get('follow_up_date', '?'))}</div><div class="k">measure again, find the next bottleneck</div></div>
</div>

<h2>Process map</h2>
<div class="card">{process_svg(d.get('steps', []) or [], bn.get('step'))}</div>

<h2>Root cause</h2>
<div class="card rc"><ol>{chain}</ol><p><strong>Actionable cause:</strong> {esc(rc.get('actionable_cause', '?'))}</p></div>

<h2>Solution</h2>
<div class="card"><p>{esc(sol.get('chosen', 'not chosen yet'))}</p></div>

<h2>Baseline{' and follow-up' if any(f.get('metrics') for f in d.get('follow_ups', []) or []) else ''}</h2>
<div class="card">{metric_table(d)}</div>

<footer>Consult Anything by Jockkie Studio · jockkie.com · Labels: seen = stated or shown, inferred = estimated, unknown = not measured yet. This dashboard is generated from your dossier and stays with you.</footer>
</main></body></html>
"""
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"Dashboard written to {sys.argv[2]}")


if __name__ == "__main__":
    main()
