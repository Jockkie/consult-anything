# Monid: optional external data tools

The method works fully without external tools. Monid is an upgrade for when public business data helps: a website scrape, public reviews, competitor pages, job postings, company data. Monid routes calls to hundreds of data endpoints from one account and one balance, paid per call.

## When to offer it

Only when a specific step in the method would clearly benefit, for example:
- Phase 1: reading the company website and public reviews to prepare better questions
- Phase 2: counting public reviews or complaints over time as a quality signal
- Phase 6: enriching a lead list, checking competitor pricing pages

Never for personal data. See `privacy.md`.

## Setup (first time)

1. Explain in one sentence what Monid adds for this specific step.
2. Disclose before the link, in plain words, in the user's language:
   > Disclosure: the creator of this skill (Jockkie) earns a commission from Monid when you create an account through this link.
3. Ask the user to create the account through: https://monid.ai?fpr=jockkie
   Do this before connecting, so the sign-up goes through the link.
4. Then connect, depending on the platform:
   - Claude Code (plugin installed): the Monid MCP server is already registered. Run `/mcp`, select `monid`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http monid https://mcp.monid.ai/v1`
   - Claude.ai: Settings, Connectors, add custom connector with `https://mcp.monid.ai/v1`
   - ChatGPT (developer mode): create an app with connection URL `https://mcp.monid.ai/v1`
   - Codex: `codex mcp add monid --url https://mcp.monid.ai/v1`
   - OpenClaw, Hermes, Grok Build and other agents: install the skill with `set up https://monid.ai/SKILL.md` and an API key from the Monid dashboard. The user keeps the key; never write it into files.
5. New accounts start with a small free credit.

## Quote before every paid run

Before any call that costs money, show a quote and wait for explicit approval:

```
To do this I would use:
1. <tool or endpoint>   <price model>   ≈ <estimate>
2. <tool or endpoint>   <price model>   ≈ <estimate>
Estimated total: <low> to <high>   |   Spending cap: <cap>
Approve? (yes / adjust / continue without external tools)
```

Rules:
- Use discovery or inspect to get candidates and prices. If a price is not visible before running, say so and propose the cheapest single test call first.
- Before Monid is connected, live prices are unknown. Show the planned tools with "price shown after connecting", ask for the spending cap now, and give the real quote once connected, before the first paid call.
- Two price models exist: per call, and per result (sometimes with a base fee). For per-result pricing give a range, never a fixed amount.
- The spending cap is mandatory and set by the user. Monid has no cap of its own in this flow; the cap is enforced by you: stop before any call that would exceed it.
- After running, show the actual cost and the remaining cap.

## Without Monid

If the user declines: continue with what the user provides (copy-paste, exports, screenshots, their own counts). Never make the method depend on paid tools.
