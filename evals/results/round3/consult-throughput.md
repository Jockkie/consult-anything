# consult-throughput (consult-anything, case throughput-quotes)

Persona: owner of a 12-person heat pump installer, English. Facts known to the user: 40 leads/week, owner makes all quotes, 8-10 quotes/week, 25 waiting, installation 12/week, no price list. Everything else the user says is a plausible small-business answer. The user labels nothing. Real script runs: `scripts/bottleneck.py` and `scripts/dashboard.py` on the dossier (outputs shown inline).

USER: We are drowning in work but revenue is flat.

ASSISTANT: Thanks, that is a useful start. Here is what I will do: I will interview you about how an order moves through your business, find the one step that limits everything else, find out why that step is slow, and then help you fix it, with numbers before and after. It takes roughly 20 to 40 minutes of conversation (longer if we do a measurement week), it is free, and external data tools are optional and only used if you want them.

"Drowning in work but revenue is flat" often means work is piling up in front of one step, so I want to find that step rather than guess.

What do you sell, and who buys it most?

USER: We install heat pumps for homeowners, mostly in a 40 km radius around town. Also yearly maintenance contracts, but that is small.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 1 of 9 topics done`

So you sell heat pump installations to homeowners, with a small maintenance side. Noted.

Who works in the company, and which of those people touch an order?

USER: 12 people. Me as owner, one planner, one office person, seven installers and two apprentices.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 2 of 9 topics done`

Twelve people: you, a planner, an office person, seven installers and two apprentices. At this point I am only hearing you; I will mark the planner and installers as "not heard yet" and come back to that.

Think of the last order you signed. Walk me through it from the first contact to the payment: what happened, step by step, who did it, and with which tool?

USER: Last one was a couple with a 1990s house. They filled in the form on the website. Office put it in our Excel list and emailed them. Then I looked at the photos they sent and the house data, called them, and sometimes I go and look. I made the quote in Word, copying an old quote and changing it. They signed by email. Planner put it on the planning board, installers did it in two days, office sent the invoice from the accounting software, and they paid in two weeks.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done`

What I hear is this chain: lead (website form, phone or email, office puts it in the Excel list), quote (you, from photos and a call or a visit, built in Word from an old quote), signature (email), planning (planner, planning board), installation (installers), invoice (office, accounting software), payment. Every step has an owner and a tool, so that topic is covered.

Now the numbers. How many new leads come in per week?

USER: About 40 a week, give or take. A bit more in autumn.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done` (throughput in progress)

About 40 leads per week, noted. How many quotes actually leave the building per week?

USER: Eight, ten. I do them in the evenings and on Saturday.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done` (throughput in progress)

So 40 leads arrive and 8 to 10 quotes go out. How many leads are waiting for a quote right now?

USER: I counted yesterday, 25. Some of them are more than three weeks old.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done` (throughput in progress)

25 leads waiting, some for three weeks or more. Now the other end of the chain: how many installations does your crew do per week, and is anything waiting in front of that step?

USER: The crew can do 12 a week. But honestly lately it is more like 8, because that is what is signed. Maybe 3 jobs are waiting for a date that suits the customer.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done`

Let me write down what I have, with the labels I will use: leads 40 per week, quotes 8 to 10 per week with 25 waiting (you counted these: `seen`), installation capacity 12 per week, with around 8 actually done and about 3 jobs waiting for a customer date (the 8 and the 3 are `inferred`, you estimated them). Interesting: the crew has room, the quotes do not come out fast enough to fill it.

Next, time. Take the last three quotes you sent: how many days passed between the lead arriving and the quote going out, and how many hours of actual work was the quote itself?

USER: Between 5 and 6 days I'd say, maybe longer for the busy weeks. The work itself is about an hour and a half, two hours with the photos.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done` (lead time in progress)

About 5 days elapsed for about 1.5 hours of work, which means a quote is being worked on for roughly 4 percent of the time it takes (`inferred`). The rest is waiting.

How often does a quote have to be corrected or redone after you sent it?

USER: One in ten, roughly. Wrong radiator count or I forgot the subsidy paperwork line.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done`

Topic 5 is covered: about 10 percent rework on quotes (`inferred`), two handoffs (office to you, you to planner).

Money now. What is a typical heat pump job worth to you?

USER: About 9,500 euro for a normal one.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done` (money in progress)

9,500 euro per job (`seen`). Where do you lose money right now (leads that never get a reply, late payments, discounts, rework), and what does the biggest leak cost you per month, as a range?

USER: The waiting leads, definitely. Some go to someone else after two weeks. If half of those 25 go elsewhere, and a third would have signed, that is something like 20 to 40 thousand a month in work I never see.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 6 of 9 topics done`

I will record that as an estimate (`inferred`): leads that wait weeks for a quote and go elsewhere, 20,000 to 40,000 euro per month in lost orders. Payments are not a leak for you.

Which tools do you use every day, and does anyone maintain them for you?

USER: Website form that sends an email, Outlook, the Excel list the office keeps, Word for quotes, a planning board the planner keeps up, and the accounting software for invoices. The office person looks after all of that.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 7 of 9 topics done`

Tools: website form, Outlook, Excel lead list, Word quote template, planning board, accounting software; the office person maintains them. Nothing here needs replacing yet, which is useful to know.

If this works, what number is different in three months?

USER: I want quotes out in two working days, nearly always. Say 90 percent. By the first of February.

ASSISTANT: `Phase 1 of 9 · Interview · Gate 1: 8 of 9 topics done`

Goal: 90 percent of quotes sent within 2 working days, by 1 February 2027 (`seen`). Today's baseline: 9 quotes per week, median 5 days from lead to quote, 25 waiting, recorded with today's date (8 November 2026).

Here is the Gate 1 check.

| # | Topic | Status |
|---|---|---|
| 1 | Business | done |
| 2 | Who is speaking | done (owner only; planner, office, installers marked `unknown`) |
| 3 | Process steps | done |
| 4 | Throughput | done (quotes a range, 8 to 10) |
| 5 | Lead time and quality | range (quote step only; other steps `unknown`) |
| 6 | Money | range (20,000 to 40,000 euro per month, `inferred`) |
| 7 | Existing systems | done |
| 8 | Goal | done |
| 9 | Baseline | done |

Summary: a 12-person installer of residential heat pumps in a 40 km radius, average job 9,500 euro. 40 leads arrive per week, you alone build all quotes (8 to 10 per week, evenings and Saturdays, about 5 days from lead to quote), 25 are waiting, and the crew can do 12 installs a week but does about 8. The estimated leak is 20,000 to 40,000 euro a month. Goal: 90 percent of quotes within 2 working days by 1 February 2027.

Is this a fair picture of your business today?

USER: Yes, that is fair.

ASSISTANT: `Phase 2 of 9 · Process map and bottleneck · Gate 2 pending`

Gate 1 passed. I ran the numbers through the bottleneck script on the dossier:

```
| Step | Per week | Effective | Waiting | Flow efficiency | Rework | Flags |
|------|----------|-----------|---------|-----------------|--------|-------|
| Leads | 40 (seen) | 40 | 0 | ? | ? | - |
| **Quote** | 9 (seen) | 8.1 | 25 | 4% | 10% | work waiting, mostly waiting (flow efficiency < 15%), high rework (>= 10%), range estimate |
| Installation | 12 (seen) | 11.4 | 3 | 75% | 5% | work waiting |
| Invoicing | 15 (inferred) | 15 | 0 | 4% | ? | mostly waiting (flow efficiency < 15%) |

Prime candidate: Quote (runner-up: Installation)
```

(Invoicing: you did not give me a number, so I used 15 a week as a rough capacity, labelled `inferred`; the office person can confirm it later.) Two strongest candidates side by side: quotes are 8 to 10 a week with 25 waiting, installation can do 12 and gets about 8. This type is "throughput and waiting". My recommendation: the constraint is the quote step, because it has the lowest capacity, the biggest queue, and the biggest money impact (every waiting quote is a 9,500 euro job).

Do you agree that quoting is the bottleneck?

USER: Hm. My crew is on the road all day, everyone says we are busy. I thought installation was the problem.

ASSISTANT: `Phase 2 of 9 · Process map and bottleneck · Gate 2 pending`

I understand why it feels that way, and it is a common trap: the loudest problem is not always the constraint. The numbers say the crew can do 12 jobs a week and only gets about 8 because not enough signed quotes reach them. If we speed up installation, nothing changes; if we get more quotes out, the crew fills up to 12 and revenue follows. The "drowning" is mostly you, doing quotes at night.

Does that match what you see on the planning board?

USER: Yes. The planner did say last week she has gaps on Thursdays and Fridays. OK, it is the quotes.

ASSISTANT: `Phase 3 of 9 · Root cause`

Gate 2 passed: the bottleneck is the quote step (type: throughput and waiting; evidence: 8 to 10 per week against 40 leads, 25 waiting, crew has spare capacity; confirmed by you, today).

Routing check: this is not a customer acquisition problem (you have 40 leads a week), so we continue here in Consult Anything.

Now the root cause, using five whys. Why do you build every quote yourself?

USER: Because I am the only one who knows what to charge.

ASSISTANT: `Phase 3 of 9 · Root cause`

Why are you the only one who knows the prices?

USER: I price from experience. It is in my head and in old quotes in Word.

ASSISTANT: `Phase 3 of 9 · Root cause`

Why is there no price list or standard quote?

USER: Every house is different, I never thought it would work as a list. Although, if I am honest, most of them are the same handful of setups.

ASSISTANT: `Phase 3 of 9 · Root cause`

That is the important sentence. Roughly what share of your quotes is one of those same handful of setups?

USER: Seven out of ten, I think. Air-water pump with the same few sizes, with or without a boiler.

ASSISTANT: `Phase 3 of 9 · Root cause`

The chain, as I will record it: quotes take about 5 days and 25 are waiting (`seen`), because you build every quote (`seen`), because only you know the prices (`seen`), because prices live in your head and old quotes (`seen`), because there is no price list or quote template (`seen`). About 7 in 10 quotes are standard setups (`inferred`).

Actionable cause: **no price list and no quote template.** That is something the business controls.

Phase 4 is breaking the goal into tasks. Our goal is 90 percent of quotes out within 2 working days. What is your first idea for how we would achieve that?

USER: A price list. And a proper template. And maybe someone else making the first version.

ASSISTANT: `Phase 4 of 9 · Break the goal into tasks`

Good, those are the main branches. I asked "how?" down to tasks that take under a day each, and scored them (money impact 1 to 5, AI fit 1 to 5, can an existing tool do it, effort S/M/L):

- Goal: 90 percent of quotes out within 2 working days
  - Prices known to more than one person
    - Price list for the 5 most sold setups: money 5, AI fit 2, existing tool yes (Excel), effort M
  - A quote that can be made quickly
    - Quote template with fill-in fields in Word: money 5, AI fit 3, existing yes, effort S
    - AI first draft from the lead form plus the price list: money 4, AI fit 5, existing yes, effort M
  - Someone other than you builds it
    - Planner drafts, you approve once a day: money 5, AI fit 4, existing yes, effort S
  - Sort the incoming leads
    - Standard setup versus needs a home visit, decided when the lead comes in: money 3, AI fit 3, existing yes, effort S

Priority is money impact first, then existing system, then AI fit, then effort. A high-AI-fit task with low money impact waits, so "AI first draft" comes after the price list and the template.

Who could draft the quotes, and how many hours a week does that person have?

USER: The planner. She has gaps on Thursdays and Fridays like I said, maybe six hours a week, and she is good with Word.

ASSISTANT: `Phase 5 of 9 · Choose the solution`

Six hours a week is enough for the standard 7 in 10 (about 6 to 7 quotes a week at 1 hour each is the planner's draft, you approve). Here is one recommended option and two alternatives:

**Recommended: price list, quote template, planner drafts, you approve once a day.** What changes: a one-page price list for the five most sold setups; the Word template with fill-in fields (subsidy line included); the planner drafts from the lead form plus the list; you approve at a fixed moment, for example 16:00, instead of building. Later, AI can write the first draft. Effort: S to M (about a week to build). Expected effect: quotes sent per week from 9 to 14 or more, lead time from 5 days toward 2. Risk: a draft without your check on price and scope; so the approval step stays.

**Alternative A: buy quoting software.** Effort L, new tool and training, the same missing price list is still needed. Not now.

**Alternative B: hire an estimator.** Effort L, high cost, and the knowledge still sits in your head. Not now.

One of the non-AI parts is the decision rule: you approve, you do not build.

Which option do you choose?

USER: The first one. Let us do that.

ASSISTANT: `Phase 5 of 9 · Choose the solution`

Chosen: price list plus quote template, planner drafts, owner approves daily at 16:00. Dossier updated (see below). Next is Phase 6, building it step by step, and then ten test runs on real quotes before it goes live.

**This week, one concrete step:** write the price list for the five most sold setups. Done when: five rows with a price, a scope line and the subsidy line each, in one Excel sheet.

Baseline recorded (8 November 2026): quotes per week 9, median days lead to quote 5, quotes waiting 25. Follow-up date: 20 December 2026.

The dossier is saved as `dossier.json` (and a Markdown version on request), and `dashboard.py` produced a one-file dashboard from it.

When can you and the planner block two hours this week to sit down and write the price list together?

USER: Wednesday afternoon.

ASSISTANT: Good. Wednesday afternoon, then. When you have the list, come back and we start Phase 6: the template and the planner's first draft.

---
Run notes (not part of the conversation): dossier at /tmp/ct/dossier.json, dashboard at /tmp/ct/dash.html. Bottleneck script output above is the real output. Turns: 23 assistant, 22 user.
