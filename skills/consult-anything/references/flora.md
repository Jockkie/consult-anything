# Flora: optional visuals for the solution

The method works fully without Flora. Offer it only when a picture makes the solution easier to use or to share with the team: a process map before and after, a dashboard mock-up, a one-page visual of the new way of working, slides for the team meeting.

## Disclosure (say this before any affiliate link, in the user's language)

> Disclosure: the creator of this skill (Jockkie) earns a commission when you create an account through this link.

Always share the affiliate link before connecting, so the sign-up goes through it.

## What Flora adds

Flora is a visual AI canvas for images, video and design. With the Flora MCP the agent can make those visuals in the company's own style.

Setup:
1. Disclosure, then the link: https://refer.flora.ai/jock-oosterveer-htu6
2. Connect the Flora MCP server `https://mcp.flora.ai/mcp`:
   - Claude Code (plugin installed): the Flora MCP server is already registered. Run `/mcp`, select `flora`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http flora https://mcp.flora.ai/mcp`
   - Claude.ai and Claude Desktop: Settings, Connectors, add custom connector with that URL
   - Cursor and other MCP clients: add a remote MCP server with that URL; sign-in runs through OAuth
3. Flora generations cost credits. Before generating, state the expected cost in dollars (Flora reports it in dollars), ask for a spending cap and get approval. Stop before any generation that would exceed the cap.

## How to brief it

- Use the company's colours and fonts if the user has them (ask once); otherwise keep it neutral and say so.
- Only what the user approved for sharing goes into a prompt: no names of staff or customers, no figures they marked confidential. See `privacy.md`.
- Never imitate another brand, real people or copyrighted characters.
- Show the visual, ask what to change, and keep the version history short: two rounds, then the user decides.
