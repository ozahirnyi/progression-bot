"""Calendar & reporting use-cases (student-owned).

This module contains computations used by:
- `/status`
- `/last14`
- `/heatmap`
"""

from __future__ import annotations

from datetime import date, timedelta

from progression_bot.domain.models import DayInfo, Plan, Schedule, State, StatusSummary


def compute_status(state: State, today: date) -> StatusSummary:
    total_minutes = sum(stage.expected_hours * 60 for stage in state.plan.stages)
    if state.start_date is None:
        done_minutes = 0
    else:
        done_minutes = sum(
            entry.minutes for entry in state.entries
            if entry.day >= state.start_date
        )
    remaining = total_minutes - done_minutes
    if remaining <= 0:
        expected_deadline_date = today
        days_to_finish = 0
        return StatusSummary(
            total_minutes,
            done_minutes,
            remaining,
            expected_deadline_date,
            days_to_finish,
        )
    if state.schedule.daily_target_minutes <= 0:
        return StatusSummary(
            total_minutes,
            done_minutes,
            remaining,
            today,
            0,
        )
    remaining_work = remaining
    expected_deadline_date = today
    days_to_finish = 0
    while remaining_work > 0:
        expected_deadline_date += timedelta(days=1)
        if expected_deadline_date.weekday() < 5:
            remaining_work -= state.schedule.daily_target_minutes
    days_to_finish = (expected_deadline_date - today).days
    return StatusSummary(
        total_minutes,
        done_minutes,
        remaining,
        expected_deadline_date,
        days_to_finish,
    )

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

