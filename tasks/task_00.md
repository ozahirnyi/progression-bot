## Task 00 — Welcome to ProgressionBot

Tiny joke first: why did the backend developer stare at the calendar? Because it had too many **dates**.

### What this project is
`progression_bot` is a Telegram bot used to track learning progress for a future Python backend developer.

This repository is intentionally a **student skeleton**:
- Telegram transport is ready (polling, routing commands).
- **All business logic is removed** (you will implement it).

### What is already implemented
- **Telegram plumbing**: `progression_bot/bot/telegram_app.py`
- **Command routing**: `progression_bot/bot/router.py`
- **Command handlers (stubs)**: `progression_bot/bot/handlers.py`
- **Fixture file (mock data)**: `fixtures/mock_state.json`
- **Placeholders to implement**:
  - `/log` parsing: `progression_bot/bot/parse.py`
  - output rendering: `progression_bot/bot/render.py`
  - heatmap PNG rendering: `progression_bot/bot/heatmap_image.py`

### Your goal (high level)
Implement the missing logic so the bot works as an MVP:
- track minutes per day (with `h`/`m` input)
- show `/status`, `/last14`, `/plan`
- generate `/heatmap` as a PNG (GitHub-style)

### Bot link
Open the bot in Telegram:
- `https://t.me/progression_88_bot`

### First steps after cloning
1. Copy `.env.example` to `.env` and fill in your `BOT_TOKEN`
2. Install dependencies: `py -m pip install -r requirements.txt`
3. Run the bot once to verify setup: `py -m progression_bot`
4. Read this file completely, then start with `task_01.md`

### How to run
1) Create `.env` in repo root (never commit it).

Example:

```env
BOT_TOKEN=put_your_token_here
TZ=Europe/Kyiv
STORAGE_PATH=./data/state.json
```

2) Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

3) Run:

```powershell
py -m progression_bot
```

### What to do next
Start from `task_01.md` and go in order.

### “Done” definition (when you can say MVP works)
The MVP is done when:
- `/log ...` updates a real JSON state file (`STORAGE_PATH`)
- `/status` shows correct totals and a projected deadline
- `/last14` shows 14 days with correct statuses
- `/heatmap` returns a PNG image in Telegram

### “Done” definition (for every task)
A task is considered **done** only when:
- **All tests for that task pass** (e.g. `py -m pytest -m task02`)
- A **PR is created**, tests are green, and it is **approved by the project owner** and merged to `main`

### Branch / PR rules (important)
- Every task must be done in a branch named exactly: `task_00`, `task_01`, `task_02`, ...
- A PR must be opened from that branch into `main`
- CI will run only the tests for your task marker:
  - branch `task_02` → `py -m pytest -m task02`
- `main` runs only tests for tasks listed in `tasks/progress.json`

### How CI knows which tasks are “done”
We track completed tasks in:
- `tasks/progress.json`

When you finish a task and its PR is ready to merge:
1) Add your marker to `tasks/progress.json`:
   - `task_02` PR → add `"task02"` to `completed_markers`
2) Merge PR to `main`

### Practice PRs (required)
Before real tasks, create **two practice PRs**:
1) **Good PR (green)**:
   - branch: `task_00`
   - make a tiny harmless change (e.g. fix a typo in a task file)
   - run: `py -m pytest -m task00`
   - open PR → it should pass CI
2) **Bad PR (red)**:
   - branch: `task_00`
   - intentionally break something (e.g. temporarily rename `tasks/task_00.md`)
   - run tests and see them fail
   - open PR → CI should fail

Goal: learn the workflow without risking real logic.
# pisun
