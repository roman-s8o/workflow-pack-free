# Demo: what the pack does on a real (tiny) project

This folder is a worked example. It uses a deliberately small project so you can read everything in a few minutes. The outputs are real: they were produced by running the pack's skills in Claude Code on the sample project, and they are not edited.

The sample is small and the run happened once. It shows how the workflow behaves, not how much it improves anything.

## The story

1. **The project.** `project/shop.py` has one function, `total(prices, discount_percent)`. The roadmap's first milestone is "correct discount calculation".
2. **The hidden bug.** The original code subtracted the discount percent from the subtotal instead of applying a percentage. The only test, `total([100], 10) == 90`, passed anyway, because 100 minus 10 equals 90. Tests were green and the Definition of Done was satisfied by accident.
3. **`/log-event`.** The failure was recorded as `E001`: what happened, with the file as evidence. See `project/.dev-os/EVENTS.jsonl`.
4. **`/fresh-review`.** An agent with no access to the author's reasoning reviewed `shop.py`. It found the real bug. It also produced one false positive (it did not look for existing tests). The result was logged as `E002`, with counts.
5. **`/audit`.** The audit read the log and found a pattern: the tests could not tell the right formula from the wrong one, and the roadmap's own Definition of Done repeated the same ambiguous example. It proposed one falsifiable hypothesis. See `audit-output.md`.
6. **`/experiment`.** The experiment skill turned that hypothesis into a plan with a baseline, a falsification condition and a list of confounders, and then stopped to ask for approval. See `experiment-plan.md`.

## Files

| File | What it shows |
|---|---|
| `project/shop.py`, `project/test_shop.py` | The fixed code and tests |
| `project/docs/ROADMAP.md` | A milestone written in the pack's format |
| `project/.dev-os/EVENTS.jsonl` | The two events, as the skills wrote them |
| `audit-output.md` | The audit report |
| `experiment-plan.md` | The experiment plan, stopped at approval |

## What this does not show

- One tiny project and one run. It does not show that the workflow saves time or improves quality.
- The audit is only as good as the events recorded. Two events are a thin base, and the audit says so itself.
- The false positive in `E002` is real. Fresh reviews are not free of noise, which is why the skill makes you check every finding.
