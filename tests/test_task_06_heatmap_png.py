from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from progression_bot.storage.json_store import JsonStore
from progression_bot.bot.heatmap_image import build_heatmap_png


@pytest.mark.task06
def test_heatmap_png_returns_png_bytes_or_skips(fixture_path: Path, fixed_today: date):
    # Heatmap PNG task typically requires Pillow. If it's not installed yet,
    # student can install it later; until then we skip.
    pil = pytest.importorskip("PIL")
    assert pil is not None

    state = JsonStore(path=fixture_path).load()
    png = build_heatmap_png(state, today=fixed_today, weeks_limit=12)
    assert isinstance(png, (bytes, bytearray))
    assert png[:8] == b"\x89PNG\r\n\x1a\n"

