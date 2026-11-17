# Self-check (visible to the user)

Run this before every gate summary and every delivery, and show the result to the user as a short block titled "Self-check". If an item fails, fix it first and say what you fixed. Never claim a check passed that you did not do.

## Checklist
1. **Sources:** every fact in the dossier comes from something the user said or showed in this conversation. Anything else is labelled `inferred` (with its basis) or `unknown`. If you can run code: `python3 scripts/check_dossier.py dossier.json --gate <1|2|deliver>` must pass.
2. **No invented numbers:** you did not fill in a figure the user did not give, and you did not change an input after seeing a script result unless the user gave a new fact.
3. **One question:** your message ends with exactly one question.
4. **Gate confirmed:** the user confirmed the summary (Gate 1) or the bottleneck (Gate 2) in their own words, not you.
5. **Gap arithmetic:** before recommending, the gap (arriving minus capacity) is shown and each option says how much of it it closes.
6. **Files:** you name only files that exist; text the user must keep is printed in full.
7. **Privacy:** no names or personal data in the dossier; health data never.
8. **Clean reply:** no notes to self, no internal codes, no announcements of what you are about to do.

Write values you do not know as `unknown` (or with label `unknown`), never leave them out; list choices you made yourself (a scope, a time window, a conversion rate) in the dossier's `assumptions` list. The assumptions block may only say "none" when that is true.

## Assumptions block (in every gate summary and delivery)
Show "What you told me and what I assumed": what the user said (with their words), what you estimated (with the basis), and what is still unknown. With code: `python3 scripts/check_dossier.py dossier.json --assumptions`.
