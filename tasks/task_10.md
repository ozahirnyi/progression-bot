# Task 10 — Implement `/plan` (Stage 2)

A plan is just a list of stages until you render it. Then it's a list of stages with expected hours.

## Goal

Show the learning plan in the bot: list of stages with names and expected hours. Command: `/plan`. Data comes from the current state (same file as `/status` and `/log`).

## Expected result

- `/plan` returns a readable list of stages and expected hours (optionally total hours at the end).
- If state was loaded from the fixture or JSON with stages, the output matches that data.

## Contract for tests

Tests expect in `progression_bot.bot.render`:

- **`render_plan_text(plan: Plan) -> str`** — takes a `Plan`, returns a string that includes each stage's name and expected hours (e.g. "1. ProgressionBot — 30 h", "2. Python backend — 40 h"). The text must not contain "TODO" or "implement" (tests will skip a stub).

You can use the plan data shape from the domain (`state.plan`, `Plan`, `PlanStage` with `name` and `expected_hours`); a separate use case for `/plan` is not required — load state, take `state.plan`, and call `render_plan_text(state.plan)` in the handler.

## Hints

- `Plan` has `stages: tuple[PlanStage, ...]`, `PlanStage` has `name: str` and `expected_hours: int`.
- Optionally show total planned hours at the end (e.g. via `plan.total_planned_minutes()` if that exists).
