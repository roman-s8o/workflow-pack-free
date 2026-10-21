# Workflow Pack — Free edition

**The test passed. The code was wrong.**

```python
def total(prices, discount_percent=0):
    subtotal = sum(prices)
    return subtotal - discount_percent   # meant: take a percentage off

assert total([100], 10) == 90            # passes: 100 minus 10 is also 90
```

This is from the demo project in this repository. The only test used the one input where the right and the wrong formula give the same answer. The plan's Definition of Done used the same example. Tests were green, the milestone looked done, and the code was wrong.

`fresh-review` is a free skill for Claude Code that catches this kind of mistake. It writes down what the work must do, gives the work to an agent that has not seen your conversation, then checks each finding and labels it real, false positive or unclear. In the demo it reviewed `shop.py` and returned 3 findings: 2 real, including this bug, and 1 false positive.

## Install

As a plugin, in Claude Code 2.1.275 or later:

```
/plugin install workflow-pack --marketplace roman-s8o/workflow-pack-free
```

In earlier versions, in two steps:

```
/plugin marketplace add roman-s8o/workflow-pack-free
/plugin install workflow-pack@tnsystems
```

Or by hand: copy `.claude/` into the root of your project. If the project already has `.claude/skills/`, copy only the `fresh-review` folder into it.

## Use

Run `/workflow-pack:fresh-review <file, diff or plan>` if you installed the plugin, or `/fresh-review <file, diff or plan>` if you copied the folder. For example: `/workflow-pack:fresh-review src/parser.py`, `/workflow-pack:fresh-review the last commit` or `/workflow-pack:fresh-review docs/PLAN.md`. The agent:

1. writes the acceptance criteria (from `docs/ROADMAP.md` if you have one, otherwise it asks you);
2. gives the reviewer only the artifact, the criteria, the relevant rules from your `CLAUDE.md` and the output format, not your conversation;
3. checks each finding itself and labels it real, false positive or unclear;
4. fixes the real findings with the smallest change and shows you the unclear ones.

"No findings" is a valid result. The agent does not ask the reviewer to try again just to get findings.

## How is it different from /code-review?

Claude Code has a built-in `/code-review`. It looks for bugs in your code changes, and its reviewer also runs without your conversation. Keep using it. `fresh-review` does a different job:

- **It checks the work against what it should do.** It writes the acceptance criteria first, and the reviewer checks the work against them. "Is there a bug?" and "Does it do what it should?" are different questions.
- **It reviews plans, not only code.** Give it a roadmap, a spec or a design note before any code exists. A blind spot is cheaper to fix in a plan than in code.
- **It shows the noise.** Every finding is checked and labelled, so you see how much of a review was useful. With the full pack, these counts go into a log that the audit reads.

## What is inside

```
.claude/skills/
└── fresh-review/SKILL.md   independent review by an agent with no shared context
.claude-plugin/             plugin files, so Claude Code can install it with /plugin
demo/                       a worked example of the full pack, with real, unedited outputs
```

See `demo/README.md` for the whole story: the bug, the review, and the audit that found the same blind spot in the plan. The demo was produced with the full pack, so it also shows the skills that are not in this free edition.

## What it does not do

- It does not replace your own review. The reviewer can be wrong; that is why every finding is checked and labelled.
- The value of a fresh review is not proven in general. The evidence so far is small: a few reviews on two projects.
- Each review costs an extra agent run, in tokens and time.

## The full pack

The full pack is for the step before the review: turning an idea into milestones with a Definition of Done you approve, and building them one at a time with verification at the end. It also keeps a log of what went wrong, so you can see what repeats and test a fix.

It adds: `roadmap` (a rough idea to a roadmap of finished, verifiable milestones), `milestone` (build one milestone with approval and verification at each step), `log-event` (a log of what went wrong), `audit` (read the log, find what repeats, propose one hypothesis), `experiment` (test the hypothesis with a baseline and a verdict), the router `CLAUDE.md`, the project-state and roadmap templates, the experiment template, and a step-by-step guide. With the full pack, `fresh-review` also records its counts in the event log for the audit.

Full pack, 39 USD: https://tnsystems.gumroad.com/l/workflow-pack

## License

MIT. See `LICENSE`.
