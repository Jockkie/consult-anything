# Solution design: tasks, build, automate, test

## 1. Task tree

Start with the goal from the dossier. Ask "how would we achieve this?" Write the answers as branches. For each branch ask "how?" again. Keep going until every leaf is a concrete action a person or system can do in under a day.

Example:
- Goal: reply to every lead within one hour
  - Know immediately when a lead arrives → notification from the web form into the shared inbox
  - Have a good first reply ready → reply templates per lead type, AI drafts a personal version
  - Someone owns replies → assign a daily owner, backup on their day off

## 2. Score each leaf

| Criterion | Scale | Question |
|-----------|-------|----------|
| AI fit | 1 to 5 | Is this repetitive, text or data based, and checkable by a human? |
| Money impact | 1 to 5 | How directly does this move the bottleneck metric or revenue? |
| Existing system | yes or no | Can a tool they already use do this? |
| Effort | S, M, L | Hours, days or weeks to set up? |

Priority = money impact first, then existing system, then AI fit, then low effort. A high AI-fit task with low money impact waits.

## 3. Choose

Offer one recommended option plus at most two alternatives. For each: what changes, effort, expected effect on the bottleneck metric, main risk. Prefer improving an existing system. Non-AI options count: remove a step, standardize, give a mandate, change an order.

## 4. Build

Build in the smallest useful slice. Typical building blocks:
- Prompt or instruction set saved as a reusable skill or custom instruction
- Template (quote, reply, report, checklist, SOP)
- Automation in an existing tool (forms, CRM rules, invoicing reminders, calendar booking)
- Small script for data cleanup or reporting
- Clear owner and mandate written down

If external data or paid tools are needed, follow `monid.md`: quote, cap, approval, then run.

Always keep a human check on anything that goes to a customer, money, or a legal commitment.

## 5. Make it run on its own

The user should not become the new bottleneck. Options, from simplest:
- A checklist in the daily routine with a named owner
- An automation rule inside a tool they already use
- A saved skill or prompt plus a scheduled routine on their AI platform, if it supports scheduling
- A script on a scheduler (only if someone can maintain it)

Write down: trigger, what happens, who checks the output, what to do when it fails.

## 6. Test ten times

AI outputs vary. One good run proves nothing.
- Run the solution ten times on realistic inputs.
- Score each run out of 10 against criteria agreed upfront (correct, complete, tone, time saved).
- Use the average. Look hard at the worst runs and fix the cause.
- After every change, run the ten tests again.
- Record the scores in the dossier under `tests`.

Below an average of 7, do not roll it out. Improve or choose a simpler option.
