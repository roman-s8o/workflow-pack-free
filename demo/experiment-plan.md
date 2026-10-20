> Raw output of `/experiment`, run in Claude Code 2.1.301 on the sample project. Not edited. The skill stopped at the approval step, as designed, before changing anything.

Phases 1 and 2 are done. I'm stopping at Phase 3 for your approval before I change anything.

## Phase 1: Hypothesis
- **If we change:** every numeric Definition of Done item in `docs/ROADMAP.md` must list two examples with different inputs.
- **then:** tests derived from those examples fail on a seeded wrong implementation.
- **because:** a single ambiguous example (100 minus 10 equals 90) hid the flat-subtraction bug (E001).
- **Success criterion:** tests built from the two-example DoD fail on 100% of the seeded wrong implementations, which are the E001 flat-subtraction bug plus the extra mutants listed below.

## Phase 2: Baseline and falsification
- **Measured:** how many seeded wrong implementations of `total()` survive (pass all tests), counted from a mutation run.
- **Baseline, from E001 and the current Milestone 1 DoD:** the DoD has one numeric example, `100 at 10% → 90`. The flat-subtraction mutant (`subtotal - discount_percent`) passes that single example, so 1 of 1 mutants survives. The current `test_shop.py` has 4 passing tests, so I'll re-measure that baseline with the single DoD example alone before any change.
- **Falsification condition (stated before the run):**
  - Any seeded mutant passes tests built strictly from the two-example DoD. That means the hypothesis is NOT SUPPORTED.
  - Or the flat-subtraction mutant already fails on the single-example baseline. That means the baseline is invalid and the result is INCONCLUSIVE.
- **Sample:** very small. It's one DoD item, one real bug (E001), and 2 or 3 synthetic mutants:
  - `subtotal - discount_percent` (E001)
  - `subtotal * discount_percent / 100` (returns the discount instead of the remainder)
  - `subtotal * (1 - discount_percent / 10)` (wrong divisor)

## Phase 3: Plan
- **Change (smallest):** I'll edit only the Milestone 1 DoD in `docs/ROADMAP.md`. The "10 percent on 100 gives 90" item becomes two examples with different inputs, for instance `100 at 10% → 90` and `50 at 10% → 45`. I'll also add the rule "numeric DoD items need two examples with different inputs" to the DoD guidance in the Milestone 2 template.
- **Measurement:**
  1. Write `/tmp` scratch copies of `shop.py` for each mutant, outside the repo.
  2. Write a test file containing only the DoD examples, once for the single-example baseline and once for the two-example version.
  3. Run pytest against each mutant with each test file and record which mutants survive.
  4. Leave the real `shop.py` and `test_shop.py` untouched.
- **Confounds and limits:**
  - **Hindsight bias:** I know the E001 bug, so I'd pick examples that catch it. To limit this, I'll pick the examples from the DoD text only, before building the mutants, and I'll report this as a limit.
  - **Mutants chosen by me:** they may be easier or harder than real bugs.
  - **Not established:** the result won't show that people or agents will follow the rule, or that it generalises beyond percentage maths.
- **Verdict handling:** at most "validated once, to be repeated". I won't make it a mandatory gate on one experiment.
- **Record (Phase 6):**
  - Create `.dev-os/experiments/2026-10-16-two-example-dod.md` from the template.
  - Update Current Experiment and Last Decision in `.dev-os/PROJECT-STATE.md`.
  - Append an `experiment_result` event to `EVENTS.jsonl` with `ref` set to E001 and E002.
- **Git:** I won't run any git commands. I'll print the commit command for you.

Do you approve this plan? Tell me if you want different mutants or example values.
