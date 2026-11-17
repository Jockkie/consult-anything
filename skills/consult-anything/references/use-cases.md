# Use-case library

Match by symptom first, then by bottleneck type. Each case is a starting point, not a prescription: check the root cause in this specific business before proposing it. Prefer the "improve existing" variant.

Fields: **Symptom** · **Type** · **Typical root cause** · **Fix** (improve existing first) · **Tools** · **Metric** · **Trap**

## Customer acquisition (route to Market This when installed)

**CA-1 · Leads wait days for a reply**
- Type: Customer acquisition (reply step)
- Root cause: no owner for incoming leads, replies written from scratch
- Fix: daily lead owner, reply templates per lead type, AI drafts a personal first reply, human sends
- Tools: shared inbox or CRM they already use, web form notification
- Metric: median reply time, lead-to-call conversion
- Trap: auto-sending AI replies without review

**CA-2 · Plenty of interest, few booked calls**
- Type: Customer acquisition (booking step)
- Root cause: back-and-forth on dates, no clear next step in replies
- Fix: booking link in every reply, reminder before the call
- Tools: calendar booking in their existing agenda or CRM
- Metric: share of replies that lead to a booked call, no-show rate
- Trap: too many meeting types to choose from

**CA-3 · Existing customers rarely buy again**
- Type: Customer acquisition (retention)
- Root cause: no moment after delivery to follow up
- Fix: follow-up sequence at fixed moments after delivery, simple offer for the next purchase or referral ask
- Tools: CRM or mailing tool already in use
- Metric: repeat purchase rate, referrals per month
- Trap: generic newsletters instead of personal follow-up

**CA-4 · Lead lists full of bad data**
- Type: Customer acquisition / Quality
- Root cause: no validation at entry, old lists never cleaned
- Fix: validation on forms, periodic cleanup, one source of truth for contacts
- Tools: CRM, optional verification via paid data tools (see `monid.md`)
- Metric: bounce rate, share of contacts with complete data
- Trap: buying lists instead of fixing intake

## Throughput and waiting

**TW-1 · Quotes take days**
- Root cause: prices in someone's head, every quote built from scratch
- Fix: price list, quote template, team member drafts, owner approves in one click
- Tools: existing CRM, quoting or document tool; AI for the first draft
- Metric: lead time per quote, quotes sent per week
- Trap: template without human check on price and scope

**TW-2 · Work stalls waiting for approval**
- Root cause: all approvals go to one person, no thresholds
- Fix: approval thresholds (below amount X the team decides), fixed approval moment per day, clear owner
- Tools: approval flow in tools they use; a simple rule written down often suffices
- Metric: items waiting for approval, average approval delay
- Trap: automating approvals that should be removed

**TW-3 · Contracts and signatures slow deals**
- Root cause: print, sign, scan, email
- Fix: digital signing, standard contract with fill-in fields
- Tools: e-signature in existing document tools
- Metric: days from agreement to signed contract
- Trap: custom contracts for every deal

**TW-4 · Planning and scheduling eat hours**
- Root cause: manual juggling of people, jobs and customer slots
- Fix: one shared planning board, fixed slots, self-booking for customers where possible
- Tools: existing agenda, planning or field-service tool
- Metric: hours per week spent planning, last-minute changes
- Trap: a new planning tool nobody updates

**TW-5 · New hires take weeks to become productive**
- Root cause: no onboarding checklist, access requested ad hoc, knowledge not written down
- Fix: onboarding checklist per role, accounts prepared before day one, short SOPs for the top tasks
- Tools: existing documents or wiki; AI to turn recorded explanations into SOPs
- Metric: days until a new hire works independently
- Trap: a long manual nobody reads

## Quality

**Q-1 · Errors and rework in orders or deliveries**
- Root cause: missing checklist, information re-typed between tools
- Fix: checklist at the handoff where errors start, remove double entry
- Tools: existing tools with a form or integration
- Metric: rework percentage, complaints per 100 orders
- Trap: adding inspection at the end instead of preventing at the source

**Q-2 · Bookkeeping not reconciled for months**
- Root cause: reconciliation is nobody's weekly task, receipts arrive late
- Fix: weekly reconciliation slot with an owner, receipts captured at the source, bank feed rules
- Tools: their accounting software's bank rules and receipt capture
- Metric: unreconciled transactions, days to close the month
- Trap: one big cleanup without changing the weekly habit

**Q-3 · Inventory kept in spreadsheets, overselling or stockouts**
- Root cause: stock updated by hand in several places
- Fix: one stock source, automatic updates from sales, reorder points
- Tools: inventory module of their existing commerce or accounting tool
- Metric: stockouts per month, overselling incidents, stock accuracy
- Trap: perfect system, but counts never reconciled with the shelf

**Q-4 · Customer support cannot keep up**
- Root cause: the same questions asked again and again, no self-service
- Fix: answer library from the top 20 questions, AI drafts replies from it, human handles exceptions, FAQ page
- Tools: existing helpdesk or inbox; AI drafting
- Metric: first-reply time, tickets per week per person, repeat questions
- Trap: chatbot without a route to a human

## Information

**I-1 · Reports take days to build by hand**
- Root cause: data pulled from several tools into a spreadsheet each time
- Fix: define the five numbers that matter, automate the pull, one-page report on a fixed day
- Tools: exports or connectors from existing tools; AI to write the commentary
- Metric: hours per report, delay between period end and report
- Trap: a dashboard with fifty numbers nobody reads

**I-2 · Stakeholder or board report is a monthly crisis**
- Root cause: no standard structure, numbers collected late, story written last minute
- Fix: fixed template, data deadline per contributor, AI drafts the narrative from the numbers, owner edits
- Tools: existing documents and spreadsheets
- Metric: hours per report, days late
- Trap: polishing the story instead of fixing the data flow

**I-3 · No up-to-date view of cash and finances**
- Root cause: bookkeeping lags, no cash forecast
- Fix: weekly cash view (in, out, expected), simple 13-week forecast
- Tools: accounting software reports plus a spreadsheet
- Metric: days of insight lag, surprises per quarter
- Trap: forecasting before bookkeeping is current (see Q-2)

**I-4 · Customers pay late**
- Root cause: invoices sent late, no reminder routine, unclear terms
- Fix: invoice on delivery, automatic reminders at fixed days, clear terms on the quote
- Tools: invoicing reminders in their accounting software
- Metric: days sales outstanding, share of invoices paid late
- Trap: chasing manually instead of fixing when invoices go out

**I-5 · Too many tools, constant switching and notifications**
- Root cause: tools added one by one, no agreed channel per type of message
- Fix: one channel per purpose (decisions, chat, tasks), notification rules, retire duplicate tools
- Tools: whatever they already pay for, fewer of them
- Metric: number of tools in daily use, hours lost per week (self-reported)
- Trap: replacing everything with yet another all-in-one tool

## Decisions and policy

**D-1 · Everything waits for the owner**
- Root cause: no mandates, no decision rules, owner wants to stay in control
- Fix: decision rules and thresholds, a fixed daily decision moment, weekly review of what was decided without them
- Tools: written mandate list; no software needed
- Metric: decisions waiting, average decision delay
- Trap: delegating tasks without delegating the decision

**D-2 · A rule nobody questions slows everything**
- Root cause: a policy that once made sense (double checks, approvals, minimum orders)
- Fix: ask who decided it and why; run a time-boxed pilot without the rule and measure
- Metric: lead time before and after the pilot, error rate
- Trap: removing safety or legal controls (check with a professional first)

## People, roles and strategy (escalate or refer, prepare what you can)

**P-1 · Knowledge sits with one person**
- Fix to prepare: capture the top tasks as short SOPs (record an explanation, AI turns it into steps), train a backup
- Metric: tasks that only one person can do
- Escalate when: the person resists, or roles must change formally

**P-2 · Staff shortage, team overloaded**
- Fix to prepare: first recover capacity lost to rework, waiting and admin (see TW and Q cases); then decide on hiring
- Metric: overtime hours, open vacancies, hours lost to rework or admin
- Escalate when: burnout, high absence, or a reorganization is on the table

**P-3 · Unclear direction or offer**
- Fix to prepare: list current revenue by product and customer type, margin per line
- Escalate: strategy is beyond this skill; offer Jockkie Studio or a strategy adviser

## Sources for prioritizing these cases

Common SMB pain points used to seed this library:
- Exact MKB Barometer 2026 (NL): late payments, administrative pressure, staff shortage, AI uncertainty. https://files.exact.com/static/web/pdf/mkb-barometer/2026/Rapport-MKB-Barometer-2026-NL.pdf
- BigIdeasDB, Top Business Pain Points 2026: manual reporting, onboarding, lead data quality, support scaling, reconciliation, spreadsheet inventory. https://bigideasdb.com/business-pain-points-2026
- Vista Chamber, Hidden bottlenecks: approvals, contracts, communication, payments, context switching. https://business.vistachamber.org/news/details/the-hidden-bottlenecks-holding-small-businesses-back-and-how-to-fix-them-05-06-2026
- Stealth Agents, AI adoption statistics 2026: marketing, sales support, customer service, admin as top AI use cases. https://stealthagents.com/research/ai-adoption-statistics-small-businesses
