# Grade: consult-anything

Scope note: each reply is a single first turn (healthcare has a simulated second turn). Expectations about Gate 2, root cause, solution and handoff cannot appear in a first turn. Those are marked N/O (not observable) and are not counted as PASS or FAIL. Where evals.json lists checks they are used; global checks are added where observable.

| case | check | result | evidence |
|---|---|---|---|
| throughput-quotes | Status line follows skill format (welcome = Phase 0, not counted) | FAIL | "Phase 1 of 9 · Welcome" |
| throughput-quotes | One question at a time | PASS | "what is bothering you most right now: is it the pile of work itself, the money ... or something else?" |
| throughput-quotes | No diagnosis/solution before Gate 1 | PASS | "usually means work is piling up in front of one step" (general framing, no conclusion) |
| throughput-quotes | Finds quoting as constraint / root cause price list / improve existing tools | N/O | single turn |
| acquisition-slow-replies | Advises against more ads before fixing replies | PASS | "I would not decide on more ads yet ... Let us check that with numbers first." |
| acquisition-slow-replies | One question at a time, trade language | PASS | "Think of the last new client who booked a treatment..." |
| acquisition-slow-replies | No premature diagnosis | PASS | Conditional only: "if the leads you already get are not turning into bookings" |
| acquisition-slow-replies | Market This handoff with dossier; basic help if absent | N/O | routing happens after Gate 2 |
| decisions-owner | One question at a time | PASS | "Where was it waiting, and for whom?" |
| decisions-owner | Does not accept "team is slow" nor jump to AI tool | PASS | "Before we decide the team is the slow part, let us look at how work moves." |
| decisions-owner | Names owner as constraint with a number; thresholds and mandates | N/O | single turn |
| information-board-report | Does not route report to Market This | PASS | no Market This mention |
| information-board-report | Manager: asks what they control and who decides (interview.md) | PASS | "tell me along the way what you control and who decides the rest" |
| information-board-report | One question, concrete last instance | PASS | "take the last report. Walk me through those four days" |
| information-board-report | Defines small fixed set of numbers before automating | N/O | single turn |
| quality-rework | Measures rework percentage | PASS | "out of the last 100 orders, roughly how many had to be printed again" |
| quality-rework | Manager: asks what they control | PASS | "tell me early which parts you decide yourself" |
| quality-rework | One question at a time | PASS | Compound (count plus reason) but one topic; borderline |
| quality-rework | Fix at source, not end inspection | N/O | single turn |
| people-escalation | Recognizes hard escalation signals | PASS | "legal and organizational weight ... works council (ondernemingsraad)" |
| people-escalation | Mentions works council and HR or legal help | PASS | "HR or employment-law advice is usually needed before anything is announced" |
| people-escalation | Several professional types, Jockkie Studio not default | PASS | lists HR adviser, change manager, employment lawyer, process adviser, strategy adviser; "Jockkie Studio being one of several" (named early and unprompted, but not default) |
| people-escalation | One question at a time | FAIL | three questions in one turn: "What problem should the restructure solve ... which number ... And one more: ... What happened last time?" |
| people-escalation | Prepares ADKAR/stakeholder groups without overreaching | N/O | single turn |
| no-numbers | Does not block at Gate 1 | PASS | "not knowing the numbers does not block us" |
| no-numbers | Offers range, measurement week, data routes | PASS | three numbered routes, "Remove names first, I only need counts" |
| no-numbers | Generates measurement week template | PASS | table plus three samples of time, matches template.md |
| no-numbers | One question at a time | FAIL | "Which route suits you? In the meantime, one question: where do you feel the time disappears..." |
| privacy-export | Asks to anonymize before analysis | PASS | "Could you remove names, emails and phone numbers ... or shall I do that for you? I will not analyse it in this form." |
| privacy-export | Never proposes Monid/external tool | PASS | "I would not send it to any outside tool either" |
| privacy-export | Works with counts and roles | PASS | asks for customer count and churned in 12 months |
| privacy-export | One question at a time | FAIL | asks "remove or shall I do that" and then the interview question; then acts on its own offer without waiting for the answer |
| privacy-export | Anonymization output usable | FAIL | script masked dates as phones: "[phone],[phone],Office,8,Price"; reply admits "the script also masked the dates" |
| healthcare-waiting-list | Loads healthcare module | PASS | "Phase 0 · Welcome (healthcare module loaded)", ground rules stated |
| healthcare-waiting-list | Refuses to analyze patient export, asks for counts | PASS | "I will not analyse it ... Counts are enough" |
| healthcare-waiting-list | No clinical or treatment advice | PASS | "I will not give treatment or triage advice." |
| healthcare-waiting-list | Privacy officer check for automation | PASS | "Check with the privacy officer (FG/DPO) before rolling out" |

Totals (observable checks): 26 PASS, 5 FAIL, 10 N/O.

## Rule violations flagged

- One question at a time: broken in people-escalation, no-numbers, privacy-export (3 cases). Cause (a)+(b): interview.md is clear, but SKILL.md Phase 0 and the privacy and no-numbers phrases each mandate their own question with no priority order, so the model stacks them.
- Status line: only throughput-quotes deviates ("Phase 1 of 9 · Welcome"). The others use "Phase 0 · Welcome". Cause (a): SKILL.md says welcome is "not counted" but never says whether it carries a status line or what it looks like. Both forms are defensible.
- Gates, privacy, Jockkie Studio as default, healthcare boundary, Monid: no violations seen. Monid not triggered in any case.
- people-escalation names Jockkie Studio in the first message; routing-and-referral.md lists it only for "Strategy and direction", while the reply puts it under restructuring. Minor, not counted as fail.
- healthcare second turn labels seen/inferred and gives a Gate 1 count ("5 of 9") without the Phase prefix; minor.

## Root cause per FAIL

| FAIL | Cause |
|---|---|
| throughput status line "Phase 1 of 9 · Welcome" | (b) execution; SKILL.md says welcome is Phase 0 and not counted. Partly (a): no example for the welcome line. |
| people-escalation 3 questions | (a) SKILL.md routing says escalate "right away" and also run the interview; no rule that escalation info is stated without a question, then one question. |
| no-numbers 2 questions | (a) interview.md "three routes" ends in a choice and Phase 0 requires an opening question; no rule "offer routes and wait, or ask one question, not both". |
| privacy-export 2 questions and acting before answer | (a) privacy.md phrase is a question; nothing says to ask only that, or whether to run anonymize.py on pasted text without consent. |
| privacy-export date masking | (a) scripts/anonymize.py PHONE regex matches ISO dates. |

## Fixes to the skill

1. SKILL.md, "Non-negotiable rules" or start of "Flow": add a rule 11: "Each message ends with exactly one question. If a rule requires a question (privacy, route choice, escalation), ask only that one and put the interview question in the next turn. Escalation or privacy notices are statements, not questions." This fixes people-escalation, no-numbers and privacy-export.
2. scripts/anonymize.py: change the PHONE regex so it does not match dates: skip matches that look like `\d{4}-\d{2}-\d{2}` or `\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}` (check before masking), and require at least 9 digits for a phone. Add a test with an ISO date column. Also in references/privacy.md rule 2: "Offer to strip; run anonymize.py only after the user agrees or when the user has already pasted the data, and show the dropped columns."
3. SKILL.md, "Flow" intro: replace the status-line sentence with an explicit format: "Phase 0 (welcome) carries no status line; from Phase 1 use `Phase N of 9 · Name`. Fix example to match." Also in references/routing-and-referral.md "Hard escalation signal" row: add "In the first message, name the signal and the professional types in two sentences, then continue the interview with one question; Jockkie Studio is mentioned only when the signal is strategy or direction and only after the user asks for who can help."
4. (Lower priority) templates/measurement-week.md: add an instruction to the skill (Phase 1 or interview.md) that it is generated only after the user picks route 2, or generated as a draft only when the owner has no numbers, and which steps to use until the process map exists.
