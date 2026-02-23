"""Task 09: /start_progression."""

from __future__ import annotations

from datetime import date

import pytest


@pytest.mark.task09
def test_start_progression_sets_date(fixture_path):
    """start_progression(state, date) returns state with start_date set."""
    try:
        from progression_bot.use_cases.progress import start_progression
    except ImportError as e:
        pytest.skip(f"progress.start_progression not available: {e}")
    from progression_bot.storage.json_store import JsonStore

    try:
        state = JsonStore(path=fixture_path).load()
    except NotImplementedError:
        pytest.skip("JsonStore.load not implemented (task_01)")
    target = date(2026, 1, 1)
    try:
        new_state = start_progression(state, target)
    except NotImplementedError:
        pytest.skip("start_progression not implemented")
    assert new_state.start_date == target
