# hackathon-kit

English · [한국어](README.md)

A kit of rules, slash commands, templates and references for running hackathons with Claude Code (and, optionally, other models as reviewers). The command bodies and rules are written in Korean.

The product itself lives in its own Git repository or hosted app. This kit covers everything around it: reading the event rules, choosing an idea, preparing sponsors, fixing demo criteria before building, verifying the demo, and producing the deck, pitch, submission and retro.

## How it works

Each event gets its own folder, `workspace/<event-slug>/`, with `hackathon.yaml` as the source of truth for dates, deadlines, language, sponsors and build policy. Commands in `.claude/commands/` read and write that folder. Nothing in a workspace may hold API keys, tokens or personal data.

A typical flow when building before the event is allowed:

```text
/init → /ideate → /demo criteria → /design → /prepare → /preflight pre-event
→ /adapt → /demo verify → /deck → /pitch → /submit draft → /preflight final
→ you submit → pitch → /retro → /archive
```

When the rules only allow building on site, planning and design happen before the event and implementation starts at the official start time. Start a new session with `/onboard` to pick an unfinished event and see what is left.

## Principles

- Demo criteria are fixed before the product exists. Expected values never come from the product's own output.
- A local or mock run is never reported as a sponsor or production result.
- The arrows above are a map, not permission. Each command reports its status and suggests the next one; it does not run it.
- Required on-screen text is checked as actually visible in a screenshot, not just present in the DOM.

## Layout

| Path | Contents |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md` | Operating rules and command inputs/outputs |
| `.claude/commands/` | Slash commands (`/init`, `/ideate`, `/design`, `/demo`, `/prepare`, `/deck`, `/pitch`, `/submit`, `/retro`, …) |
| `.claude/rules/` | Writing (Korean/English), language and design rules |
| `references/` | Workflow policy, readiness gates, model routing, and your own lists of winners, submissions and past events (empty templates) |
| `templates/` | `hackathon.yaml` and handoff templates |
| `tools/` | Presenter view and a read-only workflow checker |
| `workspace/` | Your events. Empty in this repository |

## Getting started

1. Fork or copy this repository. Keep your fork private if you will commit event workspaces.
2. Open it in Claude Code and run `/init <event URL>`.
3. Follow the suggested next command.

Tests: `python3 -m unittest discover -s tests` (needs PyYAML).

## License

MIT
