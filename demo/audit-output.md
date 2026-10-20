> Raw output of `/audit`, run in Claude Code 2.1.301 on the small sample project in `project/`. Not edited. Commit ids refer to that project's own git history and do not exist in this repository.

### Project Workflow Audit

**Lifecycle:** DISCOVERY. `PROJECT-STATE.md` still holds the unfilled template placeholders. The evidence fits an early-stage project: 2 commits, 2 events, and no milestone finished through the formal flow.

**Current state:** The shop.py discount bug is fixed, and tests now cover it and the zero-price case. Milestone 1 still has every checkbox unticked in `docs/ROADMAP.md`. `PROJECT-STATE.md` has no stage, focus, audit date or hypothesis. No experiment records exist, only the template. The workflow itself was edited in the same commit as the code fix (`e2f59ec`). That commit changed the `fresh-review` and `log-event` skills.

### Observed Patterns

1. **A weak test hid a real bug (E001, `6f8d963`).**
   - The only test, `total([100], 10) == 90`, passed against the wrong formula `subtotal - discount_percent`, because 100−10 equals 90.
   - Completion was judged by a passing suite, but the tests couldn't tell the right formula from the wrong one.
   - The roadmap's Definition of Done repeats the same example ("10 percent on 100 gives 90"), so the DoD itself can't distinguish correct from incorrect code.
   - Fixed in `e2f59ec` by adding `total([50], 10) == 45`.

2. **Project state and roadmap are out of sync with the work done.**
   - The fix and tests are committed, but the Milestone 1 checkboxes are unchecked.
   - `PROJECT-STATE.md` is still the template: no lifecycle, no current milestone, and "Last Audit: none".
   - The CLAUDE.md router depends on these files being accurate, so a future session would start from stale information.
   - The fix landed with no roadmap update, which suggests the milestone skill wasn't used to close it.

3. **Fresh review found real issues but had a false positive (E002).**
   - Of 3 findings, 2 were real and 1 was a false positive, because the reviewer didn't check the existing tests.
   - The review is valuable, but the sample is only n=1.
   - `e2f59ec` already tightened the skill: unclear findings are counted separately, and no scope creep is allowed.
   - The review also caught the E001 weakness after the fact, not before. Review came after "done" instead of acting as a gate.

4. **Workflow tooling was changed with no experiment record.**
   - Skill edits went in alongside the code fix, with no hypothesis or baseline.
   - The effect of those changes can't be measured later.
   - This is minor and expected in DISCOVERY.

### Selected Improvement Opportunity

Pattern 1. A bug passed because the tests couldn't detect it, and the roadmap's Definition of Done uses the same non-discriminating example. This is the only observed failure that reached committed code. It happened once (E001). It's measurable, cheap to experiment on, and carries the highest risk if repeated as the project grows.

I considered pattern 2 (stale state) and ruled it out as the top pick. It's real, but it's housekeeping, not a recurring failure with a measurable outcome.

### Hypothesis

**If we change:**
The `milestone` workflow's verification step so that, before a milestone is marked done, every behavioral Definition-of-Done item must be covered by at least two distinguishing examples. A distinguishing example is one where a plausible wrong implementation (for instance a flat subtraction instead of a percentage) would fail. The agent also names that wrong implementation explicitly.

**then:**
Fewer defects reach a "milestone done" state with only weak test coverage. These show up as `verification_gap` events and as real findings in post-completion fresh reviews.

**because:**
E001 happened since a single example matched both the correct and the incorrect formula. Requiring a second discriminating case, and asking "what wrong code would still pass?", targets that failure directly. It costs one extra check per behavioral DoD item.

**Success criterion:**
Over the next 3 milestones that include behavioral changes, there are 0 `verification_gap` events and 0 real fresh-review findings about test weakness. The baseline is 1 of 1 milestones with such a gap (E001). Declare failure if any one of the 3 milestones has a gap after the check was applied.

### Recommended Experiment

- **Baseline:** Milestone 1 as it stood in `6f8d963`. One test, one ambiguous example, and a hidden bug found only by fresh review (E001, E002). Count events of type `verification_gap` per milestone.
- **Change:** Add the "two distinguishing examples plus name the wrong implementation" gate to the `milestone` verification step. Write behavioral DoD items with non-degenerate numbers.
- **Run:** Apply it to Milestones 2–4 and log the outcomes through `log-event`. Record the experiment in `.dev-os/experiments/` using the template.
- **Housekeeping, before starting:** Tick the Milestone 1 boxes and fill in `PROJECT-STATE.md` (stage DISCOVERY, last audit 2026-10-16, this hypothesis). I didn't make these edits, because the audit is read-only.

The sample is small (3 milestones, and a baseline of 1), so treat a pass as encouraging, not conclusive.
