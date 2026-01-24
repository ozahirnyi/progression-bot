from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest


@pytest.fixture()
def fixture_path() -> Path:
    return Path("fixtures/mock_state.json")


@pytest.fixture()
def fixed_today() -> date:
    # Keep tests deterministic (matches the fixture example dates).
    return date(2026, 1, 24)

