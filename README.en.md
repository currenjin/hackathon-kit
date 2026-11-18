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

Publication permission is not granted by using this template. Confirm the allowed local edits, staging/commits and pushes for the target repository, branch and paths before publication. Reuse an existing explicit approval within its scope; current prohibitions take precedence. Unapproved publication stays pending without blocking permitted local work. See the [publication permission policy](references/workflow-policy.md#게시-권한).

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
| `tools/` | Presenter view, a read-only workflow checker and the member persistence CLI |
| `workspace/` | Your events. Empty in this repository |

## Getting started

1. When **Use this template** is enabled, create your own private team repository from this public baseline, then clone that team copy on each machine. Template registration is not claimed here; if the button is absent, the owner must enable it first.
2. Open it in Claude Code and run `/init <event URL>`.
3. Follow the suggested next command.

Tests: `python3 -m unittest discover -s tests` (needs PyYAML).

## Individual and team participation

Individual participation keeps the existing workflow. `/init` asks individual or team first; only teams get the main-role question, with frontend/backend choices and native free-form input in the same question. No headcount or full roster is required.

Cloning creates a local checkout of the existing remote, not a new team repository. Share event metadata, per-member role records and decisions in your private team copy; never import personal kit history. Keep credentials, host conversations and the selected-member session binding out of Git.

In a new session, `/onboard` lets you select your own record or register a new one. Every command re-reads your canonical role record; the current identity binding stays only in the session. Your main role sets priorities while allowing contributions across roles, and existing records change only on an explicit role-edit request.

Missing legacy participation mode remains unknown, and historical onboarding remains read-only. See the [participation contract](references/team-participation.md) for native question fallbacks, identity confirmation and the persistence CLI. CLI tests exercise file operations; static command tests do not verify native interactive UI.

The team member persistence CLI runs on macOS/Linux. **Windows teammates must use WSL**; native Windows Python is not supported. Follow the [execution environment instructions](references/team-participation.md#실행-환경) before team registration. The kit does not install WSL or change system settings automatically, and macOS tests are not a Windows/WSL execution receipt.

## License

MIT
