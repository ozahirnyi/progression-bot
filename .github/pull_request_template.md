## Summary
- (What did you change? Keep it short.)

## Task
- Branch name must be `task_XX` (e.g. `task_02`)
- CI will run only tests for that task: `py -m pytest -m taskXX`
- When the PR is merged, update `tasks/progress.json` to include your marker (e.g. `"task02"`).

## Checklist (required)
- [ ] Branch name is `task_XX`
- [ ] All task tests pass locally (`py -m pytest -m taskXX`)
- [ ] `tasks/progress.json` updated (adds `"taskXX"` to `completed_markers`)
- [ ] PR approved by a human reviewer

## Test evidence
Paste the command output (or screenshot) of:
- `py -m pytest -m taskXX`

