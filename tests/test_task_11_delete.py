"""Task 11: delete entry."""

from __future__ import annotations

from datetime import date

import pytest


@pytest.mark.task11
def test_delete_entry_removes_day(fixture_path):
    """delete_entry(state, day) returns state with no entry for that day."""
    try:
        from progression_bot.use_cases.progress import delete_entry
    except ImportError as e:
        pytest.skip(f"progress.delete_entry not available: {e}")
    from progression_bot.storage.json_store import JsonStore

    try:
        state = JsonStore(path=fixture_path).load()
    except NotImplementedError:
        pytest.skip("JsonStore.load not implemented (task_01)")
    day = date(2026, 1, 24)
    try:
        new_state = delete_entry(state, day)
    except NotImplementedError:
        pytest.skip("delete_entry not implemented")
    found = [e for e in new_state.entries if e.day == day]
    assert len(found) == 0
