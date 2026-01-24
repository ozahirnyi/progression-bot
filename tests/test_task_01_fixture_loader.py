from __future__ import annotations

from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore


@pytest.mark.task01
def test_load_fixture_happy_path(fixture_path: Path):
    state = JsonStore(path=fixture_path).load()
    assert state.version == 1
    assert state.tz == "Europe/Kyiv"
    assert len(state.plan.stages) > 0
    assert len(state.entries) > 0


@pytest.mark.task01
def test_load_fixture_invalid_json(tmp_path: Path):
    p = tmp_path / "broken.json"
    p.write_text("{", encoding="utf-8")
    with pytest.raises(ValueError):
        JsonStore(path=p).load()


@pytest.mark.task01
def test_load_fixture_invalid_date(tmp_path: Path):
    p = tmp_path / "bad_date.json"
    p.write_text(
        """
        {
          "version": 1,
          "tz": "Europe/Kyiv",
          "schedule": { "workdays": ["Mon"], "daily_target": "2h", "bonus_threshold": "3h" },
          "start_date": "2026-13-99",
          "plan": { "stages": [ { "name": "Stage", "expected_hours": 1 } ] },
          "entries": []
        }
        """.strip(),
        encoding="utf-8",
    )
    with pytest.raises(ValueError):
        JsonStore(path=p).load()

