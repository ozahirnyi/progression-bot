"""Progress tracking use-cases (student-owned).

This module contains *pure operations* on `State`:
- start progression (set start date)
- log time (add minutes to a day)
- edit or delete entries
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from progression_bot.domain.models import Entry, State


@dataclass(frozen=True)
class LogRequest:
    day: date
    minutes: int
    note: str | None = None


def start_progression(state: State, start_date: date) -> State:
    """Initialize progression start date.

    TODO(student): Implement.
    """

    raise NotImplementedError


def log_time(state: State, req: LogRequest) -> State:
    """Add logged minutes to the given day.

    Suggested default rule: same-day entries are *summed*.

    TODO(student): Implement.
    """

    raise NotImplementedError


def upsert_entry(state: State, entry: Entry) -> State:
    """Insert or update an entry for `entry.day`.

    TODO(student): Implement.
    """

    raise NotImplementedError


def delete_entry(state: State, day: date) -> State:
    """Remove entry for the given day (if exists).

    TODO(student): Implement.
    """

    raise NotImplementedError

