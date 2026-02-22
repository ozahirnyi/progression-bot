# Stage 2 — Full bot with real state

After the MVP (tasks 00–06), the bot can show status, last14, plan, and heatmap, and persist state to JSON. Stage 2 makes the bot **fully interactive**: one state file, logging that saves, and start date.

In Stage 2 you get **only the task description and tests**. No skeleton functions or classes are provided — you create the modules and functions yourself. The tests describe the expected interface (names and behaviour).

## Stage 2 tasks (in order)

| Task | Summary |
|------|--------|
| **task_07** | Use real storage path everywhere — all commands use `STORAGE_PATH` |
| **task_08** | Make `/log` persist — `log_time` / `upsert_entry`, wire router |
| **task_09** | Implement `/start_progression` — set start date |
| **task_10** | Implement `/plan` — render stages + expected hours |
| **task_11** | (Optional) Delete entry — `/delete YYYY-MM-DD` or `/delete yesterday` |

## Branch and CI

Same rules as Stage 1:
- Branch names: `task_07`, `task_08`, …
- PR into `main`; CI runs `pytest -m task07` (etc.).
- When a task is merged, add its marker to `tasks/progress.json` (e.g. `"task07"`).

## Done (Stage 2)

You can say Stage 2 is done when:
- All commands use the same state file (`STORAGE_PATH`).
- `/log` updates that file and replies with confirmation.
- `/start_progression` sets (or resets) the start date.
- `/plan` shows the list of stages with expected hours.
- Optionally: `/delete` removes an entry for a day.

Start with **task_07.md**.
