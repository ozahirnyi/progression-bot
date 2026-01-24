"""Calendar & reporting use-cases (student-owned).

This module contains computations used by:
- `/status`
- `/last14`
- `/heatmap`
"""

from __future__ import annotations

from datetime import date

from progression_bot.domain.models import DayInfo, Plan, Schedule, State, StatusSummary


def compute_status(state: State, today: date) -> StatusSummary:
    """Compute values for `/status`.

    TODO(student): Implement using:
    - plan total planned minutes
    - logged done minutes since start_date
    - projection on future workdays
    """

    raise NotImplementedError


def last_n_days(state: State, today: date, n: int = 14) -> tuple[DayInfo, ...]:
    """Build `/last14` data.

    TODO(student): Implement day statuses + totals.
    """

    raise NotImplementedError


def day_status(schedule: Schedule, start_date: date | None, day: date, today: date, minutes: int) -> str:
    """Return the DayStatus literal for one day.

    TODO(student): Implement rules from tasks.
    """

    raise NotImplementedError


def total_done_minutes(state: State, today: date) -> int:
    """Sum minutes from start_date up to today.

    TODO(student): Implement.
    """

    raise NotImplementedError

