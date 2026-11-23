<img src=".claude-plugin/icon.png" alt="" width="96" height="96">

# Consult Anything

*Part of [Jockkie Studio's](https://www.jockkie.com) open-source skills. I do the geeking. You get the easy part.*

> **Version 0.1.0, beta.** Tested in Claude; built to the specification of the other platforms but not yet tested there. See [Platform status](#platform-status), and please [report what you find](https://github.com/Jockkie/consult-anything/issues/new/choose).

A business consultant skill for owners and managers who want to fix a problem in their company themselves. It runs a structured interview, maps the process, finds the real bottleneck and its root cause, and turns it into a measured action plan with an optional automation, a one-file dashboard and a follow-up check after six to eight weeks.

Start by asking something like "my business is stuck, help me find out why".

Optional tools, always with your consent, a quote and a spending cap: see [Optional tools](#optional-tools).

## Install

The skill folder is `skills/consult-anything`.

**Claude Code (plugin)**
```
/plugin marketplace add Jockkie/consult-anything
/plugin install consult-anything@consult-anything
```

**Claude.ai**
Zip the `skills/consult-anything` folder and upload it in Claude's skills settings.

**Hermes Agent (plugin)**
This repository is also a portable [Agent Plugins](https://vercel.com/kb/guide/agent-plugins) package (`plugin.json`, `skills/`, `mcp.json`), which Hermes loads natively. Copy the repository into `~/.hermes/plugins/consult-anything`, then `hermes plugins enable consult-anything`. Skill only: copy `skills/consult-anything` into `~/.hermes/skills/`.

**ChatGPT (Business, Enterprise, Edu)**
Zip the `skills/consult-anything` folder and upload it under Skills, Create, Upload.

**OpenClaw**
Copy `skills/consult-anything` into `~/.openclaw/skills/` (or your workspace `skills/` folder) and start a new session.

**Grok**
Import the zipped `skills/consult-anything` folder under Skills. For Grok Build, copy the folder into `~/.grok/skills/`.

**GitHub Copilot (VS Code, Visual Studio, Copilot CLI, cloud agent)**
Copy `skills/consult-anything` into `~/.copilot/skills/` for all your projects, or into `.github/skills/` in one repository.

**Codex, Cursor, Gemini CLI and other Agent Skills clients**
Copy `skills/consult-anything` into the client's skills directory (for example `.agents/skills/`, `.cursor/skills/`, `~/.claude/skills/`).

## Platform status

| Platform | Status | What that means |
|----------|--------|-----------------|
| Claude Code | Validated | The marketplace, manifest and hook pass `claude plugin validate`; the skill was tested in evaluation rounds with Claude models |
| Claude.ai | Skill tested | The same `SKILL.md` as in the evaluations; the zip upload itself is not yet tested |
| Hermes Agent | Untested | Built to the Agent Plugins specification |
| ChatGPT, OpenClaw, Grok, GitHub Copilot | Untested | Built to the Agent Skills format |
| Codex, Cursor, Gemini CLI and others | Untested | Built to the Agent Skills format |

The guard hook only runs in Claude Code. On other platforms, the visible self-check in the skill does that job. Tried it on an untested platform? [Tell us how it went](https://github.com/Jockkie/consult-anything/issues/new/choose), whether it worked or not.

## Optional tools

Everything works without paid tools. Where they help, always with your consent, a quote and a spending cap you set:

- **[Monid](https://monid.ai?fpr=jockkie)**: public business data (your website, public reviews, competitor pages, job postings). MCP: `https://mcp.monid.ai/v1`
- **[Flora](https://refer.flora.ai/jock-oosterveer-htu6)**: visuals for the solution, such as a process map before and after, a dashboard mock-up or a one-page overview for your team. MCP: `https://mcp.flora.ai/mcp`

Both MCP servers are registered but do nothing until you authenticate them with `/mcp`.

**Disclosure:** the Flora and Monid links are affiliate links. Jockkie earns a commission when you create an account through them. The skill says so before it shares a link.

## How this skill keeps you from trusting a guess

AI tools sound sure of themselves, even when they are guessing. This skill is built to show you the difference:

1. **What you told me and what I assumed.** Every summary and every delivery separates what you said (with your own words), what the skill estimated (with its basis) and what is still unknown.
2. **A check before every step that matters.** Where the skill can run code, `check_dossier.py` or the skill's own script blocks the next step while a fact is labelled as yours without your words or a number has no label.
3. **A visible self-check** before every delivery: sources, invented numbers, one question at a time, files that really exist.
4. **In Claude Code, a guard.** A small hook sends a reply back for a fix when it asks several questions at once, contains an internal note, or claims a file was saved when none was written. It only acts in sessions where this skill is used.

A good habit with any AI advice: before you act on it, ask "Which of this did I tell you, and which did you assume?"

## Privacy

What you share stays with you. Personal data is never sent to external tools, and the files the skill makes are yours to keep. The skill asks for counts and roles, not names, and anonymizes exports first.

## Quality

Every change runs the script tests and checks on GitHub (`.github/workflows/tests.yml`). The skill itself is tested with written evaluation cases (`evals/evals.json`) and full simulated conversations, graded by a separate model; results are in `evals/results`.

What changed per version is in the [changelog](CHANGELOG.md). Want to help? Read [CONTRIBUTING](CONTRIBUTING.md). Found a security problem? Report it privately through the Security tab ([how](SECURITY.md)), not in a public issue.

## Credits

The core cycle is inspired by Nick Saraev's six-step AI consulting method, extended with Lean, Six Sigma, Theory of Constraints and ADKAR.

## The other skills

| Skill | For |
|-------|-----|
| [Market This](https://github.com/Jockkie/market-this) | Owners and makers who need more customers |
| [Copywrite Me](https://github.com/Jockkie/copywrite-me) | Anyone who needs a text that sells |
| [Find My Ikigai](https://github.com/Jockkie/find-my-ikigai) | Anyone looking for what makes life worth living |
| [Align My Astro](https://github.com/Jockkie/align-my-astro) | Anyone who likes a daily reflection |

## Need a human?

The skill refers you to the right type of professional when a problem needs one. Jockkie Studio is one of the options: helicopter view, project management and workflows, process improvement, change and innovation, go-to-market, AI implementation.

## Contact and support

- Website: https://www.jockkie.com
- Email: info@jockkie.com
- The skill is free. If it helped you: https://buymeacoffee.com/jockkie

## License

MIT
