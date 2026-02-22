"""Task 07: real storage path everywhere."""

from __future__ import annotations

from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore


@pytest.mark.task07
def test_handlers_receive_storage_path():
    """Handlers (or app) must accept a configurable storage path."""
    try:
        from progression_bot.bot.handlers import Handlers
    except ImportError as e:
        pytest.skip(f"Handlers not available: {e}")
    p = Path("data/state.json")
    # Handlers must accept storage path (or fixtures_path) at construction
    h = Handlers(fixtures_path=str(p))
    assert h.fixtures_path == str(p)


@pytest.mark.task07
def test_load_from_nonexistent_creates_or_returns_default(tmp_path: Path):
    """Loading from a path that does not exist should create default state or create file (task_03)."""
    out = tmp_path / "new_state.json"
    assert not out.exists()
    store = JsonStore(path=out)
    try:
        state = store.load()
    except NotImplementedError:
        pytest.skip("JsonStore.load not implemented (task_01/03)")
    assert state.version >= 1
    assert out.exists() or (len(state.plan.stages) == 0 and len(state.entries) == 0)
