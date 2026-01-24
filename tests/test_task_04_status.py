from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore
from progression_bot.use_cases.calendar import compute_status


@pytest.mark.task04
def test_compute_status_returns_consistent_numbers(fixture_path: Path, fixed_today: date):
    state = JsonStore(path=fixture_path).load()
    summary = compute_status(state, today=fixed_today)

    assert summary.total_minutes >= 0
    assert summary.done_minutes >= 0
    assert summary.remaining_minutes >= 0
    assert summary.total_minutes == summary.done_minutes + summary.remaining_minutes
    assert summary.expected_deadline_date >= fixed_today
    assert summary.days_to_finish == (summary.expected_deadline_date - fixed_today).days

