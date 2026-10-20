# Workflow Pack 1 — Free edition

One skill for Claude Code: `fresh-review`. It sends a file, a diff or a plan to an independent agent that has not seen your conversation, so the review is not anchored by your reasoning. Then it checks each finding and labels it real, false positive or unclear.

This is the free part of Workflow Pack 1. The full pack turns a rough idea into a roadmap of verifiable milestones and builds it one milestone at a time.

## What is inside

```
.claude/skills/
└── fresh-review/SKILL.md   independent review by an agent with no shared context
demo/                       a worked example of the full pack, with real, unedited outputs
```

## Install

Copy `.claude/` into the root of your project. If the project already has `.claude/skills/`, copy only the `fresh-review` folder into it.

## Use

Run `/fresh-review <file, diff or plan>`, for example `/fresh-review src/parser.py` or `/fresh-review the last commit`. The agent:

1. writes the acceptance criteria (from `docs/ROADMAP.md` if you have one, otherwise it asks you);
2. gives the reviewer only the artifact, the criteria, the relevant rules from your `CLAUDE.md` and the output format, not your conversation;
3. checks each finding itself and labels it real, false positive or unclear;
4. fixes the real findings with the smallest change and shows you the unclear ones.

"No findings" is a valid result. The agent does not ask the reviewer to try again just to get findings.

See `demo/README.md`, step 4: a fresh review found a real bug that a weak test hid, and one false positive. The demo was produced with the full pack, so it also shows the skills that are not in this free edition.

## What it does not do

- It does not replace your own review. The reviewer can be wrong; that is why every finding is checked and labelled.
- The value of a fresh review is not proven in general. The evidence so far is small: a few reviews on two projects.
- Each review costs an extra agent run, in tokens and time.

## The full pack

Adds: `roadmap` (a rough idea to a roadmap of finished, verifiable milestones), `milestone` (build one milestone with approval and verification at each step), `log-event` (a log of what went wrong), `audit` (read the log, find what repeats, propose one hypothesis), `experiment` (test the hypothesis with a baseline and a verdict), the router `CLAUDE.md`, the project-state and roadmap templates, the experiment template, and a step-by-step guide. With the full pack, `fresh-review` also records its counts in the event log for the audit.

Full pack: https://tnsystems.gumroad.com/l/workflow-pack-1

## License

MIT. See `LICENSE`.
