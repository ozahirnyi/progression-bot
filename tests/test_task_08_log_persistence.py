"""Task 08: /log persists."""

from __future__ import annotations

from datetime import date

import pytest

from progression_bot.domain.models import Entry, State


@pytest.mark.task08
def test_log_time_adds_minutes(fixture_path, fixed_today: date):
    """log_time(state, LogRequest(day, minutes)) increases that day's total."""
    try:
        from progression_bot.use_cases.progress import LogRequest, log_time
    except ImportError as e:
        pytest.skip(f"progress.log_time / LogRequest not available: {e}")
    from progression_bot.storage.json_store import JsonStore

    try:
        state = JsonStore(path=fixture_path).load()
    except NotImplementedError:
        pytest.skip("JsonStore.load not implemented (task_01)")
    req = LogRequest(day=fixed_today, minutes=60)
    try:
        new_state = log_time(state, req)
    except NotImplementedError:
        pytest.skip("log_time not implemented")
    total_today = sum(e.minutes for e in new_state.entries if e.day == fixed_today)
    assert total_today >= 60


@pytest.mark.task08
def test_upsert_entry_replaces_or_adds(fixture_path):
    """upsert_entry(state, entry) ensures that day has the given entry (replace or add)."""
    try:
        from progression_bot.use_cases.progress import upsert_entry
    except ImportError as e:
        pytest.skip(f"progress.upsert_entry not available: {e}")
    from progression_bot.storage.json_store import JsonStore

    try:
        state = JsonStore(path=fixture_path).load()
    except NotImplementedError:
        pytest.skip("JsonStore.load not implemented (task_01)")
    day = date(2026, 1, 25)
    entry = Entry(day=day, minutes=45, note="test")
    try:
        new_state = upsert_entry(state, entry)
    except NotImplementedError:
        pytest.skip("upsert_entry not implemented")
    found = [e for e in new_state.entries if e.day == day]
    assert len(found) >= 1
    assert found[0].minutes == 45
