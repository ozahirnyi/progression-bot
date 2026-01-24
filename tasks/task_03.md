## Task 03 — Persist state to a real JSON file

Joke: saving state is like making coffee—if you forget it, you will **regret it later**.

### Goal
Stop using the fixture as “the real source of truth”.
Create a persistent state file (not committed) and read/write it safely.

### What to implement
- Use `STORAGE_PATH` from `.env` (default: `./data/state.json`).
- If the state file doesn’t exist:
  - create it from defaults (or from the fixture)
  - ensure the `data/` directory exists
- Implement:
  - load state
  - save state (prefer atomic write: write temp file, then replace)

### Expected result
After you run `/log 2h`, restarting the bot keeps that entry.

### Test cases
- Delete `data/state.json`, start bot, run `/status` → bot does not crash (creates empty state).
- Run `/log 2h` twice → the stored value for today is either:
  - **sum** rule: 4h total (recommended), or
  - replace rule (if you choose it) — but document your choice.
- Restart bot → `/last14` includes today with correct minutes.

