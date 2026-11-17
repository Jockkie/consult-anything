# consult-throughput (consult-anything, case throughput-quotes)

USER: We are drowning in work but revenue is flat.

ASSISTANT: Welcome. I will work with you like a consultant would, but you do the steering: I ask questions one at a time, we find the one step that holds the whole business back, find out why it is that way, and turn it into a plan with numbers you can check. It takes roughly 20 to 40 minutes of conversation, it is free, and external data tools are optional (nothing paid happens without your approval). I only need counts, durations and amounts, no customer names.

"Drowning in work but revenue flat" is the sentence I will test against numbers. To begin: what do you sell, and to whom?

USER: We install heat pumps for homeowners. 12 people, one location. Project price plus a yearly maintenance contract.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 1 of 9 topics done

So: heat pump installer, 12 people, one location, homeowners as customers, income from the project price plus a yearly maintenance contract. Right.

What is your own role in the company?

USER: I'm the owner. I also make all the quotes myself.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 2 of 9 topics done

Noted: you are the owner, and every quote goes through you. I have only heard the owner so far; I will mark the planner, installers and office as "not heard".

Think of the last customer who signed. What happened from first contact to payment, step by step?

USER: Customer fills in the website form or emails. I read it, call or visit, then build the quote in Word. Once they say yes, the planner schedules the installation in a spreadsheet, two installers go out, the office invoices from the accounting software.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done

What I hear is a chain of four steps: Leads (you, website form and email), Quote (you, Word), Installation (planner and two installers, planning spreadsheet), Invoicing (office, accounting software). Every step has an owner and a tool.

Next the numbers. How many new leads come in per week?

USER: About 40 a week.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done

About 40 leads per week, noted as your own figure. How many quotes leave the building per week?

USER: 8 to 10 quotes a week.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done

8 to 10 quotes per week against 40 leads. How many people are waiting for a quote right now?

USER: 25 are waiting.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done

25 waiting for a quote. And on the other side: how many installations can your teams do per week?

USER: The teams do 12 installations a week.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done

12 installations per week. Throughput is now covered for the steps you could put a number on.

From a request coming in to the quote going out, how long does that take? Roughly is fine.

USER: Around five days, though I don't really know. An hour or two of actual work each, I guess.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 6 of 9 topics done

I will record that as an estimate, not as a fact: about 5 days from request to quote, 1 to 2 hours of real work per quote (I use 1.5). That is about 4% of the time spent actually working on it, the rest is waiting. For rework and the invoicing step I have nothing yet, so those stay "unknown" instead of me guessing.

What is a typical job worth to you?

USER: Around 9,000 euros a job.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 7 of 9 topics done

About 9,000 euros per job, your figure. Which tools or spreadsheets already run part of the business?

USER: Website form, email, Word, the planning spreadsheet and the accounting software. Nothing really tried. There's no price list, I price each job from experience.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 8 of 9 topics done

Five existing tools, nothing tried yet to fix this, and no price list: you price each job from experience. I will keep that last point, it matters later.

If this works, what number is different in three months?

USER: Every customer gets a quote within two days, by the end of January.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 9 of 9 topics done

**Gate 1 checklist**

| Topic | Status |
|---|---|
| 1 Business | done |
| 2 Who is speaking | done (owner; planner, installers, office not heard) |
| 3 Process steps | done |
| 4 Throughput | range (leads 40, quotes 8 to 10, installation 12; invoicing unknown) |
| 5 Lead time and quality | range (quote lead time 5 days and 1.5 hours work are estimates; rework unknown) |
| 6 Money | done (9,000 per job; monthly leak unknown) |
| 7 Existing systems | done |
| 8 Goal | done (quote within two days for every customer by 31 January 2027) |
| 9 Baseline | done (8 to 10 quotes per week, 25 waiting, about 5 days to a quote) |

**Summary:** A heat pump installer with 12 people at one location, selling to homeowners for about 9,000 euros a job. Every lead goes through the owner, who builds every quote in Word. About 40 leads come in per week, 8 to 10 quotes leave and 25 wait. Installation can handle 12 per week. There is no price list.

**Self-check:** sources checked against what you said (pass, script run: 10 stated, 3 estimated, 16 unknown); no invented numbers (pass, invoicing and rework left empty); one question (pass); privacy (no names in the notes, pass).

**What you told me and what I assumed**
You told me: 40 leads a week ("About 40 a week."), 8 to 10 quotes a week, 25 waiting, 12 installations a week, about 9,000 euros a job, and your goal ("Every customer gets a quote within two days, by the end of January.").
I estimated (please check): 5 days from request to quote and 1.5 hours of work per quote, both from your "I don't really know" answers.
Still unknown: rework, invoicing capacity, queues in front of installation, what waiting leads cost per month.

Is this a fair picture of your business today?

USER: Yes, that's fair.

ASSISTANT: Phase 2 of 9 · Process map and bottleneck · Gate 2: waiting for your confirmation

Process map, built from your numbers:

| Step | Per week | Waiting | Flow efficiency | Label |
|---|---|---|---|---|
| Leads | 40 | unknown | unknown | seen |
| **Quote** | **8 to 10 (9 mid)** | **25** | **4% (estimate)** | seen / inferred |
| Installation | 12 | unknown | unknown | seen |
| Invoicing | unknown, left out | unknown | unknown | unknown |

Forty requests arrive per week and about 9 quotes leave. Installation can handle 12, so it is not the limit: it can do more than the quote step feeds it. That is why you are busy yet revenue is flat: the work you are drowning in is waiting for quotes, while the installers have room. The loudest problem (busy installers) is not the constraint; quoting is, and it is you personally. At 9,000 euros a job, every quote that waits is money that may go to someone else. I do not know how much, so I am not putting a number on it.

My recommendation: the bottleneck is the Quote step. The second candidate is installation at 12 per week, which has no queue number yet and is lower priority because it can handle more than it receives. Do you agree that quotes are the bottleneck?

USER: Yes, quotes are the problem. That matches what I see.

ASSISTANT: Phase 3 of 9 · Root cause · Gate 2 passed

Confirmed: the Quote step. This is a throughput and waiting problem, so we continue here; it is not a "get more customers" problem. More ads would only lengthen the queue.

Let us find why. Why do you build every quote yourself?

USER: I'm the only one who knows what to charge.

ASSISTANT: Phase 3 of 9 · Root cause · Gate 2 passed

Why is it only you who knows what to charge?

USER: It's all in my head, every job is a bit different. We never made a price list.

ASSISTANT: Phase 3 of 9 · Root cause · Gate 2 passed

That is something the business controls, so I stop asking why. The chain: 25 waiting and 5 days, because you build every quote, because only you know the prices, because they live in your head, because there never was a price list. The cause we can act on: **no price list and no quote template**. Is that how you see it?

USER: Yes.

ASSISTANT: Phase 4 of 9 · Tasks

Goal: a quote within two days for every customer. Asking "how?" down to tasks, with a score each (money impact and AI fit 1 to 5, whether you already have a system for it, effort):

| Task | Money impact | Existing system | AI fit | Effort |
|---|---|---|---|---|
| Write a price list for the most sold configurations | 5 | yes (Word or a spreadsheet) | 2 | M |
| Quote template in Word with fill-in fields | 5 | yes | 3 | S |
| Planner drafts, you approve in one daily slot | 5 | yes | 2 | S |
| AI first draft of the quote text, human checks price and scope | 3 | yes | 5 | M |

The high-AI-fit task has the lowest money impact, so it waits. Before I compute what each option closes, I need one fact: how many hours per week could the planner spend on drafting quotes?

USER: Maybe 10 hours a week.

ASSISTANT: Phase 5 of 9 · Choose the solution

The gap: 40 requests arrive, about 9 quotes leave, so up to 31 per week pile up (that is the upper limit, because I do not know how many requests really need a quote). Your 9 quotes at about 1.5 hours is roughly 13 of your hours a week (estimate).

**Self-check:** gap arithmetic shown (pass); no invented numbers: the 45 minutes per quote below is an assumption of mine, not your number, and the first week of use tests it (pass, labelled); one question (pass).

What I assumed: with a price list and template a standard quote takes about 45 minutes instead of 90 (assumption, to be measured).

**Recommended: price list + Word template, planner drafts, you approve in one daily slot.** Effort small to medium, all in tools you already have. Planner at 10 hours and 45 minutes per draft is about 13 extra quotes per week. You keep drafting the odd ones. Roughly 13 of the 31 gap, so about 22 per week in total, not 40. Risk: a template without a check on price and scope; you keep the approval.

Alternative 1: **fixed-price standard packages quoted straight from the form.** Effort medium. It could close much of the rest, but how many of the 40 requests are standard is unknown, so I cannot say how much. Risk: customers who are not standard.

Alternative 2: **quoting software.** Effort large, new tool to maintain, and it still needs a price list first. It closes nothing the recommended option does not, so I do not recommend it now.

None of the three, on today's numbers, closes the full 31 on its own; the first closes roughly 13 and the second may close more once we know the standard share. Which option do you choose?

USER: The first one, price list and template. Let's start there.

ASSISTANT: Phase 6 of 9 · Build

Good. Smallest useful slice: a price list for the configurations you sell most. Which are your most sold heat pump configurations, say the top five?

USER: Air-water 6 kW, air-water 8 kW, air-water 10 kW, a hybrid with the existing boiler, and a ground source one.

ASSISTANT: Phase 6 of 9 · Build

Here is the structure, you fill in the prices (I do not invent them):

Price list (spreadsheet, one row per configuration): configuration, heat pump price, standard installation price, extras (extra pipe metre, buffer vessel, electrical work), total from, valid until. Five rows to start: air-water 6, 8 and 10 kW, hybrid with the boiler, ground source.

Quote template (Word, fill-in fields): header with customer and address fields, the chosen configuration, price from the list, extras, what is not included, validity, one signature line. The planner fills the fields from the price list and enquiry; you check price and scope.

Who in your office could own the price list, so it stays current?

USER: The planner can own it, I'll sign off the first version.

ASSISTANT: Phase 7 of 9 · Make it run on its own, test ten times

How it runs without you: Trigger: a new request in the inbox. What happens: the planner drafts from the price list and template. Who checks: you, one slot per day. If it fails: nonstandard jobs go to your own pile and the planner flags them.

Test plan: take ten real recent enquiries, draft each one with the new list and template, and score each out of 10 on correct price, complete scope, readable, and time spent. Roll out at an average of 7 or higher and re-test after every change. This is your first week's job, so I record the tests as "to do", not as results.

What do you want to hand over to the team first: just the price list, or the whole draft-and-approve routine?

USER: The whole routine, I'll tell the planner Monday.

ASSISTANT: Phase 8 of 9 · Team, baseline, deliverables

For Monday's talk with the planner: say what changes (the planner drafts, you approve once a day), why (25 waiting and 5 days to a quote cost jobs worth about 9,000 euros each), and that the price list is the planner's to keep. It is a small change and only one person's role shifts, so no formal change plan is needed.

**Self-check (before delivery):** sources (pass, script run, 10 stated / 4 estimated / 16 unknown); no invented numbers (pass); one question (pass); files named only exist (dossier.json and dashboard.html written in your working folder; the rest is printed below); privacy (pass).

**Diagnosis (contains no customer data)**
Quotes are the bottleneck: 8 to 10 leave per week while about 40 requests arrive and 25 are waiting (stated by you), at about 9,000 euros per job. Type: throughput and waiting. Confirmed by the owner, 8 November 2026. Root cause: no price list and no quote template. Uncertain: the 5 days and 1.5 hours are estimates; a measurement week on quote times would firm them up.

**Action plan**
Goal: a quote within two days for every customer by 31 January 2027, from about 5 days (estimate) today.
This week: tell the planner on Monday, then write the first version of the price list for the five configurations; the planner starts it, you sign off. Done when the five rows have prices.
Tasks: price list (money 5, M), Word template (money 5, S), planner drafts and you approve daily (money 5, S), AI first draft of text (money 3, M, later).
Test plan: ten runs scored out of 10, roll out at 7 or higher.
Baseline (8 November 2026): 8 to 10 quotes per week (stated), 25 waiting (stated), about 5 days to a quote (estimate). Follow-up: 20 December 2026, six weeks out. On that date, start Consult Anything again and share the dossier; I will measure the same three numbers.

Files: `dossier.json` and the one-file `dashboard.html` (process map, bottleneck, baseline) are in the working folder. A readable Markdown version of the diagnosis and plan is the text above; copy it.

**What you told me and what I assumed**
You told me: 40 leads, 8 to 10 quotes, 25 waiting, 12 installations, about 9,000 euros a job, your goal. I estimated: 5 days to a quote, 1.5 hours of work, and my 45 minutes per draft (to be measured). Unknown: rework, invoicing, installation queue, what waiting leads cost.

Proposed update for your `business-context.md` (copy it, I have not changed any of your own files): "Heat pump installer, 12 people, one location, homeowners, about 9,000 euros per job. Goal by 31 January 2027: every customer gets a quote within two days. Constraint: quoting; price list in progress."

Where do you want to go from here: continue on your own with the plan, look for a professional (I can name the type), or something else?

USER: I'll continue on my own. This was useful.

ASSISTANT: Then you have what you need: the confirmed bottleneck, the cause, one step for this week and a date to measure again (20 December 2026). One line, only because you found it useful: the skill is free and can be supported at https://buymeacoffee.com/jockkie. Good luck on Monday.


## SCRIPT RUNS
(dossier states s1.json = at Gate 1, s2.json = Gate 2 confirmed, dossier.json = delivery)

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/check_dossier.py s1.json --gate 1 --assumptions
### What you told me and what I assumed

**You told me:**
- business ("We install heat pumps for homeowners. 12 people, one location. Project price plus a yearly maintenance contract.")
- steps[Leads].throughput per week: 40 ("About 40 a week.")
- steps[Quote].throughput per week: 8 to 10 ("8 to 10 quotes a week.")
- steps[Quote].queue: 25 ("25 are waiting.")
- steps[Installation].throughput per week: 12 ("The teams do 12 installations a week.")
- steps[Installation].capacity per week: 12 ("The teams do 12 installations a week.")
- money.value per order: 9000 ("Around 9,000 euros a job.")
- goal: every customer ("Every customer gets a quote within two days, by the end of January.")
- baseline.metrics[Quotes per week]: 8 to 10 ("8 to 10 quotes a week.")
- baseline.metrics[Quotes waiting]: 25 ("25 are waiting.")

**I estimated (please check):**
- steps[Quote].lead time days: 5 (based on: owner: 'Around five days, though I don't really know')
- steps[Quote].work time hours: 1.5 (based on: owner: 'an hour or two of actual work each, I guess')
- baseline.metrics[Days from request to quote]: 5 (based on: owner estimate, 'I don't really know')

**Still unknown:**
- steps[Leads].queue
- steps[Leads].lead time days
- steps[Leads].work time hours
- steps[Leads].rework pct
- steps[Quote].rework pct
- steps[Installation].queue
- steps[Installation].lead time days
- steps[Installation].work time hours
- steps[Installation].rework pct
- steps[Invoicing].throughput per week
- steps[Invoicing].queue
- steps[Invoicing].lead time days
- steps[Invoicing].work time hours
- steps[Invoicing].rework pct
- money.leaks[0]
- money.leaks[0].per month

CHECK PASSED · seen 10 · inferred 3 · unknown 16
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/bottleneck.py s1.json
| Step | Capacity per week | Effective | Arriving | Waiting | Flow efficiency | Rework | Flags |
|------|-------------------|-----------|----------|---------|-----------------|--------|-------|
| Leads | 40 (seen) | 40 | 40 | ? | ? | ? | - |
| **Quote** | 9 (seen) | 9 | 40 | 25 | 4% | ? | work waiting, mostly waiting (flow efficiency < 15%), range estimate |
| Installation | 12 (seen) | 12 | 9 | ? | ? | ? | - |
| Invoicing | ? (unknown) | ? | 9 | ? | ? | ? | capacity unknown: not ranked |

Prime candidate: Quote
Flow efficiency assumes 8 working hours per day.
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/check_dossier.py s1.json --gate 2
CHECK FAILED (2): fix these before continuing.
- Gate 2: no bottleneck named
- Gate 2: the user has not confirmed the bottleneck
[exit 1]

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/check_dossier.py s2.json --gate 2
CHECK PASSED · seen 10 · inferred 4 · unknown 16
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/check_dossier.py dossier.json --gate deliver --assumptions
### What you told me and what I assumed

**You told me:**
- business ("We install heat pumps for homeowners. 12 people, one location. Project price plus a yearly maintenance contract.")
- steps[Leads].throughput per week: 40 ("About 40 a week.")
- steps[Quote].throughput per week: 8 to 10 ("8 to 10 quotes a week.")
- steps[Quote].queue: 25 ("25 are waiting.")
- steps[Installation].throughput per week: 12 ("The teams do 12 installations a week.")
- steps[Installation].capacity per week: 12 ("The teams do 12 installations a week.")
- money.value per order: 9000 ("Around 9,000 euros a job.")
- goal: every customer ("Every customer gets a quote within two days, by the end of January.")
- baseline.metrics[Quotes per week]: 8 to 10 ("8 to 10 quotes a week.")
- baseline.metrics[Quotes waiting]: 25 ("25 are waiting.")

**I estimated (please check):**
- steps[Quote].lead time days: 5 (based on: owner: 'Around five days, though I don't really know')
- steps[Quote].work time hours: 1.5 (based on: owner: 'an hour or two of actual work each, I guess')
- baseline.metrics[Days from request to quote]: 5 (based on: owner estimate, 'I don't really know')
- bottleneck: Quote capacity 8 to 10 per week against 40 leads arriving and 25 waiting; installation capacity 12 per week (based on: capacity and queue stated by the owner; flow efficiency derived from an estimated 5 day lead time)

**Still unknown:**
- steps[Leads].queue
- steps[Leads].lead time days
- steps[Leads].work time hours
- steps[Leads].rework pct
- steps[Quote].rework pct
- steps[Installation].queue
- steps[Installation].lead time days
- steps[Installation].work time hours
- steps[Installation].rework pct
- steps[Invoicing].throughput per week
- steps[Invoicing].queue
- steps[Invoicing].lead time days
- steps[Invoicing].work time hours
- steps[Invoicing].rework pct
- money.leaks[0]
- money.leaks[0].per month

CHECK PASSED · seen 10 · inferred 4 · unknown 16
[exit 0]

$ python3 /home/claude/jockkie-studio/plugins/consult-anything/skills/consult-anything/scripts/dashboard.py dossier.json dashboard.html
Dashboard written to dashboard.html
[exit 0]
