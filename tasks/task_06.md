## Task 06 — Implement `/heatmap` as a PNG (GitHub style)

Joke: why do we render PNG? Because monospace grids in Telegram are… a **pixel-perfect lie**.

### Goal
Generate a stable heatmap image and send it as a Telegram photo:
- `/heatmap` (full period)
- `/heatmap 12` (last 12 weeks)
- Today has a blue border

### What to implement
In `progression_bot/bot/heatmap_image.py`:
- Implement `build_heatmap_png(...) -> bytes`
- Use a graphics library (recommended: Pillow)
- Layout:
  - 7 rows (Mon..Sun)
  - week columns aligned by Monday (GitHub-like)
  - month labels optional (nice to have)

In `progression_bot/bot/telegram_app.py`:
- Update `/heatmap` handler to `reply_photo(...)` using the PNG bytes.

### Dependency
If you choose Pillow, add it to `requirements.txt`:
- `pillow>=10.0.0`

### Test cases
- `/heatmap` returns a photo (not text).
- `/heatmap 12` returns a smaller photo (12 weeks).
- Today’s cell has a visible blue border.
- Colors change correctly for missed/partial/done/bonus/weekend/empty.

