from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore
from progression_bot.use_cases.calendar import last_n_days


@pytest.mark.task05
def test_last14_returns_14_days(fixture_path: Path, fixed_today: date):
    state = JsonStore(path=fixture_path).load()
    days = last_n_days(state, today=fixed_today, n=14)
    assert len(days) == 14


@pytest.mark.task05
def test_last14_is_contiguous(fixture_path: Path, fixed_today: date):
    state = JsonStore(path=fixture_path).load()
    days = last_n_days(state, today=fixed_today, n=14)
    assert days[-1].day == fixed_today
    assert days[0].day == date(2026, 1, 11)

