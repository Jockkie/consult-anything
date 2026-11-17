# consult-throughput (consult-anything, case throughput-quotes)

USER: We are drowning in work but revenue is flat.

ASSISTANT: Hi, I'm going to act as your business consultant. I'll interview you, find the one step that limits your business, find out why it is that way, and turn it into a plan you can measure. It takes about 20 to 40 minutes of conversation, it is free, and external data tools are optional (I won't use any unless you approve). If you have a business-context file or an earlier dossier, share it and I'll skip what I already know.

What bothers you most right now, in your own words?

USER: Like I said, we're busy all the time, everyone's running around, but the money coming in doesn't grow.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 0 of 9 topics done

Busy but flat revenue: so work goes in, but not more money comes out. Let me start with the basics. What do you sell, and to whom?

USER: We install heat pumps. Homeowners mostly. We're 12 people.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 1 of 9 topics done (business, to be confirmed)

So: heat pump installation for homeowners, 12 people. Which role are you in the company?

USER: I'm the owner.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 2 of 9 topics done

Got it, you are the owner. I'll note that I have only heard the owner so far; other roles are `unknown` for now. Think of the last customer who signed. What happened from first contact to the invoice, step by step?

USER: They filled in the form on the website or emailed. Then I looked at it, called or visited if needed, made a quote in Word, sent it. If they said yes the planner puts it on the planning board, installers do the job, the office sends the invoice.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done

What I hear: lead (form or email) → owner looks, calls or visits → owner makes the quote in Word → customer says yes → planner schedules on the planning board → installers install → office invoices. Is that right, and is the owner the only one who makes quotes?

USER: Yes that's right. And yes, I make all the quotes myself.

ASSISTANT: (Note to self: that was a joined ask in my last message, so counting it as asked and answered; from here, one question per message.)

Phase 1 of 9 · Interview · Gate 1: 3 of 9 topics done

Steps and owners are clear: lead (owner), quote (owner, Word), scheduling (planner, planning board), installation (installers), invoicing (office). Now numbers. How many new leads come in per week?

USER: About 40 a week.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done

40 leads per week, `seen` (your statement). How many quotes do you get out per week?

USER: Eight, maybe ten if I push.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 4 of 9 topics done

8 to 10 quotes per week. I record that as a range you gave me. How many requests are waiting for a quote right now?

USER: Around 25.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done

25 waiting for a quote, `seen`. How many installations do you complete per week?

USER: Twelve a week.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done

12 installations per week, `seen`. How long does a typical quote take from request to the customer receiving it?

USER: I don't really know. Some go out in a few days, some sit for a week or more. I don't track it.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 5 of 9 topics done

Fine, I record lead time and the hands-on work time per quote as `unknown`. We can firm that up later with a short measurement week if you want. What is a typical order worth to you?

USER: Around 9,000 euro.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 6 of 9 topics done

About EUR 9,000 per order, `seen`. Where do you think you lose money now?

USER: Probably leads that go cold because they wait too long for a quote. I can't say how much.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 6 of 9 topics done

Leads going cold while waiting is the leak you suspect, amount `unknown`. Which tools do you use every day?

USER: Email, Word, the website form, and the planning board. No CRM.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 7 of 9 topics done

Systems: website form, email, Word, planning board. Do you have a price list or a quote template you work from?

USER: No price list. I do it from experience and look at old quotes.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 7 of 9 topics done

Noted: no price list, prices come from your experience and old quotes (`seen`). If this works, what number is different in three months?

USER: I want quotes out within two working days, for nearly all of them. Say nine out of ten.

ASSISTANT: Phase 1 of 9 · Interview · Gate 1: 9 of 9 topics done (the baseline is recorded today, 2026-11-08: 8 to 10 quotes per week, 25 waiting)

Here is the Gate 1 check.

| # | Topic | Status |
|---|-------|--------|
| 1 | Business | done |
| 2 | Who is speaking | done (owner only; planner, installers, office `unknown`) |
| 3 | Process steps | done |
| 4 | Throughput | done (invoicing `unknown`) |
| 5 | Lead time and quality | unknown (no lead time or rework numbers) |
| 6 | Money | done (EUR 9,000 per order; leak amount `unknown`) |
| 7 | Existing systems | done |
| 8 | Goal | done: 90% of quotes out within 2 working days by 2027-02-08 |
| 9 | Baseline | done, 2026-11-08 |

Summary: a 12-person heat pump installer. 40 leads per week arrive, you make every quote yourself in Word with no price list at 8 to 10 per week, 25 are waiting, and installation handles 12 per week. Orders are worth about EUR 9,000. You want 9 in 10 quotes out within two working days by 8 February 2027.

Is this a fair picture of your business today?

USER: Yes, that's fair.

ASSISTANT: Phase 2 of 9 · Process map and bottleneck · Gate 2: not yet confirmed

Gate 1 passed. Let me run the numbers on the process map.

[ran scripts/bottleneck.py, output in SCRIPT RUNS]

| Step | Per week | Waiting | Label | Note |
|------|----------|---------|-------|------|
| Leads | 40 | unknown | seen | |
| **Quote** | 8 to 10 | 25 | seen | 40 arrive, 9 leave |
| Installation | 12 | unknown | seen | only gets what the quotes pass on (about 9) |
| Invoicing | unknown | unknown | unknown | left out of the ranking |

My recommendation: quoting is the bottleneck, because 40 leads arrive and only 8 to 10 quotes leave, with 25 waiting, while installation can do 12 and gets fewer than that. Installation is the second candidate; it is not the constraint, it is under-fed. Do you agree that quoting is the constraint?

USER: Hm. But we're drowning in work. Isn't installation the problem? The installers are always busy.

ASSISTANT: Phase 2 of 9 · Process map and bottleneck · Gate 2: not yet confirmed

Fair question. Installation can do 12 a week, but only about 9 quotes become jobs' worth of work per week at most, so busy installers means they are running at the speed quotes feed them. Speeding up installation would change little, because nothing waits in front of it that you told me about; the 25 waiting are in front of quotes. How many jobs are waiting on the planning board for installation right now?

USER: Not many. Two or three.

ASSISTANT: Phase 2 of 9 · Process map and bottleneck · Gate 2: not yet confirmed

2 to 3 waiting for installation, `seen`, versus 25 waiting for a quote. That backs the picture: the queue sits in front of the quote. Do you confirm that quoting is the bottleneck?

USER: Yes, I see it. Quoting it is.

ASSISTANT: Phase 2 of 9 · Process map and bottleneck · Gate 2 passed (quote confirmed; installation has a number, 12 per week, as runner-up)

Confirmed and recorded as `seen` with type "throughput and waiting".

Routing check: this is not a customer acquisition problem (you have 40 leads a week), so we continue here in Consult Anything.

Phase 3 of 9 · Root cause

Why do quotes wait?

USER: Because I make all of them.

ASSISTANT: Phase 3 of 9 · Root cause

Owner makes all quotes (`seen`). Why the owner and not someone else?

USER: Because I'm the only one who knows what to charge.

ASSISTANT: Phase 3 of 9 · Root cause

Only you know the prices (`seen`). Why do only you know them?

USER: It's in my head and in old quotes. We never wrote a price list. Every job feels a bit different.

ASSISTANT: Phase 3 of 9 · Root cause

That is a cause you control, so I stop here. The chain: quotes wait → owner makes every quote → only the owner knows what to charge → prices live in your head and old quotes → there is no price list and no quote template. Actionable cause: **no price list and no quote template**. Do you agree that this is the root?

USER: Yes. That's it.

ASSISTANT: Phase 4 of 9 · Break the goal into tasks

Goal: 9 in 10 quotes out within 2 working days. How would we achieve that? One path from the root cause: someone else must be able to draft a quote. What would they need in front of them?

USER: A price list for the usual jobs, I guess, and a quote form they can fill in.

ASSISTANT: Phase 4 of 9 · Break the goal into tasks

Task tree, from your answer:
- Goal: 9 in 10 quotes out within 2 working days
  - Anyone can draft a quote → price list for the most sold configurations (money impact 5, existing system: a Word or spreadsheet you have, AI fit 3, effort M)
  - Anyone can draft a quote → Word quote template with fill-in fields (money 5, existing: Word, AI fit 4, effort S)
  - Owner only checks → fixed approval moment per day (money 4, no tool needed, AI fit 1, effort S)
  - Leads without a quote get seen quickly → daily sweep of the 25 waiting (money 4, existing: email, AI fit 2, effort S)

Which of your team could draft a quote once there is a price list?

USER: The planner. She knows the jobs well.

ASSISTANT: Phase 5 of 9 · Choose the solution

The planner, role noted. Based on the use-case match "Quotes take days" (TW-1), I recommend this:

**Recommended: price list + Word template, planner drafts, you approve.** Effort: price list M, template S. Expected effect: quotes per week go from 8 to 10 up toward the 40 leads that arrive; the 25 waiting can be worked down. Risk: a wrong price or scope in a drafted quote, so you still check every quote before it goes out. No new software, you use Word, which you already have.

Alternatives: (1) quoting software, effort L, risk that nobody maintains it and it fits your jobs poorly now; (2) hire an estimator, effort L and costly, and the price list would still be needed first.

Which option do you choose?

USER: The first one. Price list and template, planner drafts.

ASSISTANT: Phase 6 of 9 · Build

Good, option one. We build the smallest useful slice first: the quote template. I'll draft it, you fill the real prices in, because I don't have your prices and I won't invent any.

Quote template (Word):
- Customer and address (fill in)
- Chosen configuration (pick from price list: line A, B, C ...)
- Price per configuration line (from the list; list not yet built)
- Extras (fill in, with a price from the list or "to be priced by owner")
- Validity: 30 days
- Approved by: owner, date

For the price list: which five configurations do you sell most?

USER: Mostly air-to-water, a few hybrids, and then the full replacement of the old boiler. I'd have to look at my old quotes to give the exact five.

ASSISTANT: Phase 6 of 9 · Build

That is a fine job for this week. Pull the last 30 quotes, group them by configuration, and write down the typical price for each of the top five. I'll keep the price list as a table you fill in, with columns configuration, typical price, extras, who may deviate. No external tools are needed, so there is no quote or spending cap to approve.

Phase 7 of 9 · Make it run on its own, test ten times

How it runs without you: Trigger: a new lead arrives in your inbox. What happens: the planner picks it up daily, drafts the quote from the price list and template. Who checks: you, at one fixed approval moment a day. If it fails: you take over that quote and note the gap in the price list.

Test plan: when the price list exists, run ten real leads through it, score each out of 10 on correct price, complete, and time saved, and use the average. Below 7 we do not roll out. I can't run these tests yet because the price list does not exist, so they are in the action plan, not done.

Phase 8 of 9 · Team, baseline, deliverables

How would you explain this to the planner in two sentences?

USER: "You'll draft the quotes from a price list and I'll just check them. That frees me up and gets answers to customers faster."

ASSISTANT: Phase 8 of 9 · Team, baseline, deliverables

Good and clear. Now the deliverables. Everything below is also in the dossier (JSON and a readable Markdown version).

**Diagnosis · Heat pump installer · 2026-11-08**

**Quotes are the bottleneck: 8 to 10 leave per week while 40 leads arrive and 25 are waiting (all `seen`, as stated by you). The cost in lost orders is `unknown`; at about EUR 9,000 per order, each quote that does not go out in time is real money.**

| Step | Owner | Per week | Waiting | Flow efficiency | Rework | Label |
|------|-------|----------|---------|-----------------|--------|-------|
| Leads | Owner | 40 | unknown | unknown | unknown | seen |
| **Quote** | Owner | 8 to 10 | 25 | unknown | unknown | seen |
| Installation | Installers | 12 | 2 to 3 | unknown | unknown | seen |
| Invoicing | Office | unknown | unknown | unknown | unknown | unknown |

Root cause (five whys): quotes wait, owner makes every quote, only the owner knows what to charge, prices in head and old quotes. Actionable cause: **no price list and no quote template**.

What this means: installation is only as busy as the quotes feed it. Speeding it up would change little. Fixing the quote step moves the whole business.

Uncertainty: lead times, rework and invoicing are `unknown`; a measurement week on quotes would firm them up.

**Action plan**
Goal: quotes out within 2 working days, from unknown (8 to 10 per week, 25 waiting) to 90% by 2027-02-08.
This week: **pull your last 30 quotes and write down the typical price for the top five configurations** · who: you · done when: the five prices are on one page.
Tasks: price list (impact 5, existing system, AI 3, M, owner, week 1); Word template (5, yes, 4, S, owner with planner, week 1); daily approval moment (4, yes, 1, S, owner, week 2); sweep of the 25 waiting leads with the template (4, yes, 2, S, planner, week 2).
Test plan: ten runs on real leads, scored out of 10, roll out at 7 or higher.
Baseline (2026-11-08): quotes per week 8 to 10 (seen), waiting 25 (seen), lead time unknown. Follow-up date: 2026-12-20, six weeks out.

I ran the dashboard script (see SCRIPT RUNS) and it produced dashboard.html with the process map and the baseline.

Proposed updates to your business-context.md: business is a 12-person heat pump installer; goal, 90% of quotes within 2 working days by 2027-02-08; latest from Consult Anything: bottleneck Quote, status plan made, follow-up 2026-12-20. Shall I add these?

USER: Yes, add them.

ASSISTANT: Phase 8 of 9 · Team, baseline, deliverables

Added. Routing close: this is solved here in Consult Anything. If later you want help beyond the quote fix, for example the sales flow, Market This could take the dossier; I won't push it, and it is your call. For follow-up, on 2026-12-20 start again with the dossier and we repeat the same measurements. I can't set a reminder on this platform, so please put it in your agenda. Your files: dossier.json, the Markdown version and dashboard.html.

Did you find this useful?

USER: Yes, very.

ASSISTANT: Good. One line: the skill is free and can be supported at https://buymeacoffee.com/jockkie. That is all; the work is yours now.


## SCRIPT RUNS

$ python3 scripts/bottleneck.py dossier.json
| Step | Capacity per week | Effective | Arriving | Waiting | Flow efficiency | Rework | Flags |
|------|-------------------|-----------|----------|---------|-----------------|--------|-------|
| Leads | 40 (seen) | 40 | 40 | ? | ? | ? | - |
| **Quote** | 9 (seen) | 9 | 40 | 25 | ? | ? | work waiting, range estimate |
| Installation | 12 (seen) | 12 | 9 | ? | ? | ? | - |
| Invoicing | ? (unknown) | ? | 9 | ? | ? | ? | capacity unknown: not ranked |

Prime candidate: Quote
Flow efficiency assumes 8 working hours per day.

$ python3 scripts/dashboard.py dossier.json dashboard.html
Dashboard written to dashboard.html
