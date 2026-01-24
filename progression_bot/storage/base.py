"""Storage interfaces.

TODO: keep IO details here, keep domain pure.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol


@dataclass(frozen=True)
class StoredEntry:
    day: date
    minutes: int
    note: str | None = None


class ProgressRepository(Protocol):
    def get_all(self) -> list[StoredEntry]:
        """Return all entries."""

    def upsert(self, entry: StoredEntry) -> None:
        """Insert or update an entry."""

