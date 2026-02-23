# Task 07 — Use real storage path everywhere (Stage 2)

One state file to rule them all — one JSON on disk.

## Goal

All commands that read or write bot state must use **one path from config** (`STORAGE_PATH`, e.g. `./data/state.json`). So `/status`, `/last14`, `/plan`, `/heatmap`, and later `/log` and `/start_progression` all work with the same file.

## Expected result

- After starting the bot, calling `/status` (or `/last14`, `/plan`) loads state from `STORAGE_PATH`. Changes to the file (by hand or via future `/log`) show up on the next command.
- Handlers (or router) receive the storage path from config; in tests you can use a temp path or the fixture path so real data is not touched.
- If the state file does not exist yet, loading must create a default state file (as in task_03) or return default state and create the file on first save.

## Contract for tests

Tests verify:

- That handlers (or app) accept a configurable storage path (e.g. passed at construction).
- That loading from a path where the file does not exist yields a default state or creates the file.
- That writing state to a temp file and calling the handler with that path yields the expected data (e.g. correct entry count or `start_date`).

Where you store the path (handlers class, router, config) and how you pass it into `JsonStore` is up to you — just avoid hardcoded `fixtures/mock_state.json` for production.

## Hints

- Config already has a field for the storage path; in `main.py` you can pass it when creating Handlers / Router.
- For tests you can use `tmp_path` (pytest) or a separate fixture path.
