# Deliverables

The user receives five things, usable without anyone to explain them. Write them in the user's language. On Claude, offer them as a document; on other platforms, as Markdown files.

| Deliverable | Content | Template |
|-------------|---------|----------|
| Diagnosis | One page: bottleneck, type, root cause, evidence with labels `seen`, `inferred`, `unknown` | `templates/diagnosis.md` |
| Process map | All steps with throughput, queue and flow efficiency; the bottleneck clearly marked | In the dashboard, or a table in the diagnosis |
| Action plan | Tasks with their scores, the first step for this week, who does it, the test plan | `templates/action-plan.md` |
| Baseline | Today's numbers and the follow-up date | Part of the action plan and the dossier |
| Dossier | Structured record for Market This, follow-up, referral | `templates/dossier.json` plus a Markdown version |

## Dashboard (optional)

If you can run code: `python3 scripts/dashboard.py dossier.json dashboard.html` builds one self-contained HTML file with the process map, the bottleneck, the baseline and, at follow-up, before versus after. On Claude it can be shown as an artifact; elsewhere the user opens the file in a browser.

If you cannot run code: present the process map as a table and mark the bottleneck in bold.

## Quality bar

- The first sentence of the diagnosis states the bottleneck and its number.
- Every number carries its label.
- The action plan has one step the user can do this week.
- Nothing in it requires a consultant to interpret.
