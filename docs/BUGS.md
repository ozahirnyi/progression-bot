# Bugs to fix

## Bug 1: `/last14`, `/plan`, `/status` fail when state file has `daily_target: "0m"`

**Steps to reproduce:**
1. Delete `data/state.json` (or ensure it does not exist)
2. Run the bot once — it creates a new state file with default `daily_target: "0m"`, `bonus_threshold: "0m"`
3. In Telegram, send `/last14`, `/plan`, or `/status`

**Actual result:**
```
ValueError: Minutes must be > 0
```

Commands crash; the user gets no reply.

**Expected result:**
Commands work and return a normal response (even when `daily_target` is 0). The bot should either:
- allow `parse_duration_to_minutes` to accept 0 for schedule fields when loading from JSON, or
- use a different parsing path for schedule fields that permits 0

**Root cause:**  
`JsonStore.load()` uses `parse_duration_to_minutes()` for `daily_target` and `bonus_threshold`. That function rejects 0 (valid for `/log`, where 0 makes no sense). The default state created for new users has 0, so loading fails.

**Where:**  
`progression_bot/storage/json_store.py` (load), `progression_bot/bot/parse.py` (parse_duration_to_minutes)
