
from __future__ import annotations

import io
from datetime import date, timedelta, datetime

from PIL import Image, ImageDraw

from progression_bot.use_cases.calendar import total_done_minutes, day_status

"""
TODO(student):
- Implement PNG generation for `/heatmap` using a graphics library (e.g. Pillow).
- Use `fixtures/mock_state.json` as the input fixture for local work.

Recommended UX rules:
- Colors:
  - missed (workday, 0h) -> red
  - partial (0<h<2h) -> yellow
  - done (2h<=h<3h) -> green
  - bonus (>=3h) -> darker green
  - weekend (no-plan) -> dark gray
  - empty (future/before start) -> gray
- Today should have a blue border (even if it is yellow/green).
"""



def build_heatmap_png(*args, **kwargs) -> bytes:  # noqa: ANN002, ANN003
    state = kwargs.get("state") or args[0]
    today = kwargs.get("today") or args[1]
    weeks = kwargs.get("weeks", None)
    if weeks is None:
        weeks = kwargs.get("weeks_limit")
    if weeks is None and len(args) >= 3:
        weeks = args[2]
    minutes_by_day = {}
    for entry in state.entries:
        minutes_by_day[entry.day] = minutes_by_day.get(entry.day, 0) + entry.minutes
    if weeks is not None:
        start = today - timedelta(days=weeks*7 -1)
    else:
        start = state.start_date or today
    end = today
    grid_start = start - timedelta(days=start.weekday())
    grid_end = end + timedelta(days=(6 - end.weekday()))
    cols = ((grid_end - grid_start).days // 7) + 1
    cell = 14
    gap = 2
    margin = 10
    width = margin*2 + cols*(cell+gap) - gap
    height = margin*2 + 7*(cell+gap) - gap
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)
    colors = {"missed": "red",
              "partial": "yellow",
              "done": "green",
              "bonus": "darkgreen",
              "weekend": "darkgray",
              "empty": "gray",
    }
    total_days = (grid_end - grid_start).days
    for offset in range(0, total_days + 1):
        d = grid_start + timedelta(days=offset)
        col = offset // 7
        row = d.weekday()
        x0 = margin + col*(cell+gap)
        y0 = margin + row*(cell+gap)
        x1 = x0 + cell
        y1 = y0 + cell
        minutes = minutes_by_day.get(d, 0)
        status = day_status(state.schedule, state.start_date, d, today, minutes)
        fill = colors.get(status, "gray")
        draw.rectangle([x0, y0, x1, y1], fill=fill)
        if d == today:
            draw.rectangle([x0, y0, x1, y1], outline="blue", width=2)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()