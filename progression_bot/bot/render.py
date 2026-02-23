"""Rendering (student-owned).

This repository is now prepared as a *skeleton* for the student:
- Telegram transport + routing remains.
- Business logic (status calculations, calendar rules, heatmap rendering) is TODO.

See `tasks/` and `fixtures/mock_state.json`.
"""

from __future__ import annotations

from datetime import date

from progression_bot.domain.models import DayInfo, Plan, StatusSummary


def render_status_text(summary: StatusSummary) -> str:
    """Render `/status` text from a computed summary.

    TODO(student): Implement using domain + use-cases.

    Expected output (text):
    - Total planned hours
    - Done hours
    - Remaining hours
    - Days to finish + expected deadline date (dynamic)
    """

    return (
        "TODO: implement /status\n"
        "- Compute StatusSummary in use_cases/calendar.py\n"
        "- Return a human-friendly text summary\n"
    )


def render_last14_text(days: tuple[DayInfo, ...]) -> str:
    """Render `/last14` text from day info list.

    TODO(student): Implement a detailed list for last 14 days:
    - date, weekday, status (missed/partial/done/bonus), duration, optional note
    """

    return "TODO: implement /last14 (last 14 days details)\n"


# render_plan_text(plan: Plan) -> str — you implement this for task_10 (see tasks/task_10.md)


def render_heatmap_caption(today: date, weeks_limit: int | None) -> str:
    """Caption for heatmap image.

    TODO(student): In Telegram we want a PNG heatmap (GitHub style) with:
    - colors for missed/partial/done/bonus/weekend/empty
    - blue border for today
    - optional: `/heatmap N` weeks limit
    """

    limit = f"last {weeks_limit} weeks" if weeks_limit else "full period"
    return f"Heatmap ({limit}). Today: {today.isoformat()} (blue border)."

