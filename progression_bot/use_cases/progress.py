"""Progress tracking use-cases (student-owned).

This module should contain pure operations on State:
- start_progression(state, start_date) -> State  (task_09)
- log_time(state, req: LogRequest) -> State     (task_08)
- upsert_entry(state, entry: Entry) -> State    (task_08)
- delete_entry(state, day: date) -> State       (task_11)

See tasks/task_08.md, task_09.md, task_11.md. No skeleton implementations — you add these.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from progression_bot.domain.models import Entry, State


@dataclass(frozen=True)
class LogRequest:
    """Request to log time for a day (used by task_08 tests and your log handler)."""
    day: date
    minutes: int
    note: str | None = None
