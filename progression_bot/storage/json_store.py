"""JSON storage (student-owned).

This module should:
- load `State` from JSON (fixture or real state file)
- save `State` back to JSON (real state file)

Implementation notes:
- Prefer *atomic writes* (write temp file, then replace).
- Keep JSON schema versioned.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from progression_bot.domain.models import State


@dataclass(frozen=True)
class JsonStore:
    """Filesystem-backed JSON store."""

    path: Path

    def load(self) -> State:
        """Load state from JSON.

        TODO(student):
- Parse dates and durations.
- Validate schema version.
- Return a `State` instance.
        """

        raise NotImplementedError

    def save(self, state: State) -> None:
        """Save state to JSON (atomic).

        TODO(student):
- Ensure parent dir exists.
- Write to temp file.
- Replace original file atomically.
        """

        raise NotImplementedError


def load_fixture(path: str | Path = "fixtures/mock_state.json") -> State:
    """Convenience helper for loading the fixture."""

    return JsonStore(path=Path(path)).load()

