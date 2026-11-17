# Interview and Gate 1

The interview is the most important phase. A wrong picture here means fixing the wrong thing later.

## How to interview

- One question at a time. Wait for the answer.
- Ask for numbers, examples and recent cases, not opinions. "How many quotes did you send last week?" beats "Are quotes slow?"
- Mirror back after every topic: "So what I hear is ... Is that right?"
- Use their words for steps and roles. Do not rename their world.
- If an answer is vague, ask for the last concrete instance: "Think of the last customer who signed. What happened from first contact to invoice?"
- Keep a running status line: `Gate 1: 5 of 9 topics done`.
- If the person is a manager, not the owner, ask what they control and who decides on the rest.

## The nine topics

| # | Topic | What to learn | Done when |
|---|-------|---------------|-----------|
| 1 | Business | What they sell, to whom, revenue model, team size, locations | Summarized and confirmed by the user |
| 2 | Who is speaking | Their role, which roles have not been heard yet | At least one role per main step heard, or marked `unknown` |
| 3 | Process steps | From first contact to payment (or their equivalent chain): who does each step, with which tool | Every step has an owner and a tool |
| 4 | Throughput | Units per week per step, what is waiting in front of each step | Every step has a number, a range, or `unknown` |
| 5 | Lead time and quality | Lead time versus actual work time, rework or error percentage, number of handoffs | Filled per step or `unknown` |
| 6 | Money | Value per customer or order, where revenue leaks (lost leads, late payments, discounts, rework) | At least one amount or range |
| 7 | Existing systems | Tools, spreadsheets, automations already in place, and who maintains them | List complete according to the user |
| 8 | Goal | What must be different in three months, as a number with a date | Goal with metric, target and date |
| 9 | Baseline | The numbers we will measure against later | Recorded in the dossier with today's date |

## Question bank

Pick, adapt, translate. Never ask them all.

**Business**
- What do you sell, and who buys it most?
- How many people work here, and in which roles?
- Where does most of your revenue come from?

**Process**
- Walk me through the last order from first contact to payment. What happened, step by step?
- Who touches it at each step? Which tool do they use?
- Where does work wait for someone?

**Throughput and queue**
- How many new leads, orders or requests come in per week?
- How many get through each step per week?
- What is waiting right now in front of each step? How many?

**Lead time and quality**
- How long does a typical order take from start to finish? How much of that is actual work?
- How often does something come back to be redone? Roughly what share?
- How many times does an order change hands?

**Money**
- What is a typical order or customer worth?
- Where do you lose money now: leads that never get a reply, late payments, discounts, rework?
- What do you think the biggest leak costs per month? A range is fine.

**Decisions and people**
- Which decisions wait for you personally?
- What would stop if one specific person were sick for two weeks?

**Systems**
- Which tools do you use daily? Any spreadsheets that run part of the business?
- What have you already tried to fix this?

**Goal**
- If this works, what number is different in three months?

## When the numbers are missing

Most owners do not know their weekly throughput. Never block on it. Offer three routes:

1. **Range estimate.** Ask for low and high per step. Record as `inferred`. The diagnosis states the uncertainty.
2. **Measurement week.** Generate `templates/measurement-week.md` for the steps in question. The user tallies for one week, then returns with the dossier.
3. **Show the data.** Exports from CRM, agenda, invoicing or mailbox counts. Apply `references/privacy.md` first: anonymize before sharing.

Gate 2 later requires at least the two strongest bottleneck candidates to have a number or range.

## Department heads (optional)

If the owner cannot answer for a department, offer `templates/department-questionnaire.md`, filled in for that role. The user forwards it. Answers come back into the dossier labeled by role.

## Gate 1 check

Before Phase 2, show the nine topics with a status (`done`, `range`, `unknown`) and the one-paragraph summary. Ask: "Is this a fair picture of your business today?" Only continue after a yes, or after correcting what they change.
