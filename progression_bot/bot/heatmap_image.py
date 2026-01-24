"""Heatmap image rendering (student-owned).

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

from __future__ import annotations


def build_heatmap_png(*args, **kwargs) -> bytes:  # noqa: ANN002, ANN003
    """Return PNG bytes for the heatmap.

    TODO(student): Implement.
    """

    raise NotImplementedError("TODO: implement heatmap PNG rendering")
