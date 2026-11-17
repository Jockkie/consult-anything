# Root cause

The bottleneck says where. The root cause says why. Aim the solution at the cause, not the symptom.

## Five whys (default)

Start from the bottleneck symptom and ask "why?" until you reach something the business can act on. Usually three to five rounds.

Example:
1. Quotes take five days. Why? → The owner prepares every quote.
2. Why the owner? → Only she knows the prices.
3. Why only she? → Prices live in her head and old emails.
4. Why? → There was never a price list; each job felt unique.
Actionable cause: no price list and no quote template. Fix: build a price list and a template, let a team member draft, owner approves.

Rules:
- Each answer must be a fact or a stated belief, labeled `seen` or `inferred`.
- Stop at the first cause the business controls. "The market" or "people" is not a cause; ask one more why.
- If two causes appear, follow both briefly and pick the one with more impact on the bottleneck metric.

## Fishbone (when causes are many or disputed)

Group possible causes under six headings and ask the user which are real:
- **Method:** procedures, order of steps, approvals
- **People:** skills, availability, mandate, single points of failure
- **Tools:** software, spreadsheets, missing integrations
- **Information:** missing, late or inconsistent data
- **Environment:** seasonality, suppliers, regulations
- **Measurement:** what is not measured or measured wrongly

Then rank the confirmed causes by impact on the bottleneck metric and pick one.

## Record

Store the chain in the dossier under `root_cause` with method, steps and the chosen actionable cause.
