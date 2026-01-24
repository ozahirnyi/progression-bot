from __future__ import annotations

from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore


@pytest.mark.task03
def test_save_and_reload_roundtrip(tmp_path: Path, fixture_path: Path):
    # Load from fixture, save to a new state file, then reload.
    state = JsonStore(path=fixture_path).load()

    out = tmp_path / "state.json"
    store = JsonStore(path=out)
    store.save(state)

    loaded = store.load()
    assert loaded.version == state.version
    assert loaded.tz == state.tz
    assert loaded.schedule.workdays == state.schedule.workdays
    assert loaded.plan.stages == state.plan.stages


@pytest.mark.task03
def test_save_creates_parent_dir(tmp_path: Path, fixture_path: Path):
    state = JsonStore(path=fixture_path).load()

    out = tmp_path / "nested" / "state.json"
    JsonStore(path=out).save(state)
    assert out.exists()

