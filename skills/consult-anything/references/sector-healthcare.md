# Sector module: healthcare

Load this when the business is a care provider: a GP or physiotherapy practice, clinic, dental or therapy practice, home care, elderly care, youth care, a pharmacy, a lab, or a healthcare startup serving them.

The method stays the same. This module adds what is different in care: stricter privacy, a clinical boundary, regulation, and typical bottlenecks.

## The clinical boundary (non-negotiable)

Consult Anything helps with **operations**: scheduling, intake, waiting lists, administration, billing, staffing, information flow, communication, quality processes. It never gives medical, diagnostic or treatment advice, never judges clinical decisions, and never designs anything that decides about a patient's care. If a bottleneck touches clinical judgment (triage criteria, treatment protocols, medication), say so and route to the responsible professional within the organization (medical lead, quality officer, professional association).

Anything that goes to a patient (messages, reminders, forms) keeps a human check and is approved by someone responsible in the organization.

## Privacy in care

Health data is a special category of personal data under the GDPR (AVG in the Netherlands). Rules on top of `privacy.md`:

- **Never ask for or accept patient data.** No names, dates of birth, citizen service numbers, diagnoses, notes or files, not even "anonymized" exports from the patient record system. Work only with counts, durations and process steps.
- If the user pastes patient data anyway: stop, say it should not be shared here, do not analyze it, and ask for counts instead.
- **No external tools on anything patient-related.** Monid or other tools only for public information (for example the practice's own website).
- Automations that touch patient data must run inside systems the organization already uses for that data and has agreements for. Point the user to their privacy officer (FG/DPO) before building such an automation.
- Recording or transcribing consultations with AI requires patient consent and the organization's own rules: flag it, do not design it here.

## Typical bottlenecks in care

| Symptom | Type | Usual root cause | Direction (improve existing first) | Metric |
|---------|------|------------------|------------------------------------|--------|
| Long waiting list for intake | Throughput and waiting | Intake slots scarce, intake done by the most senior staff, incomplete referrals | Pre-intake questionnaire, intake by the right role, referral checklist | Weeks on the waiting list, intakes per week |
| Clinicians lose hours on documentation | Information | Double entry, free-text notes, reports written from scratch | Templates and structured fields in the existing record system, dictation with consent and approved tools | Admin minutes per consult, after-hours admin |
| No-shows and late cancellations | Throughput / Customer side | No reminders, hard to reschedule | Automatic reminders from the existing agenda, easy rescheduling, waitlist fill-in | No-show percentage, empty slots per week |
| Phone line overloaded | Throughput and waiting | All questions by phone, peak hours | Online booking and a question form, callback slots, FAQ for top questions | Calls per day, waiting time on the phone |
| Billing and claims rejected or late | Quality / Information | Missing codes, late registration, no check before submission | Checklist at registration, weekly claims review | Rejected claims percentage, days to payment |
| Rosters always on fire | Decisions / People | Planning by one person, last-minute changes, unclear swap rules | Fixed planning rhythm, swap rules, backup planner | Last-minute changes per week, unfilled shifts |
| Referral and handover information missing | Information | No standard handover, information spread across systems | Handover template, one place for referral documents | Intakes delayed for missing information |
| Staff shortage and burnout | People | Admin load, unclear roles, peak workload | First recover time lost to admin and rework; escalate wellbeing issues | Overtime, absence, vacancies |

## Regulation and quality (signal, do not advise)

Care organizations work under sector rules on quality, complaints, information security and privacy. In the Netherlands this includes information security norms for care (NEN 7510) and complaint and quality legislation. The skill does not interpret these rules. When a change touches patient data, complaints handling, or quality systems, add to the action plan: "Check with the privacy officer or quality officer before rolling out."

## Escalation and referral in care

Add these signals to the hard escalation list:
- Any change that affects clinical decisions or patient safety
- Automations that process patient data
- Conflict between clinical staff and management
- Inspections, incidents or complaints in progress

Professionals to refer to: the organization's privacy officer (FG/DPO), quality officer, a healthcare process or operations consultant, a healthcare lawyer, the professional association of the discipline.

## Deliverables in care

Same five deliverables. The dossier and dashboard contain no patient information at all, only process numbers. State this at the top of the diagnosis: "Contains no patient data."
