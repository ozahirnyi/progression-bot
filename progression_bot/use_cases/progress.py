"""Progress tracking use-cases (student-owned).

This module should contain pure operations on State:
- start_progression(state, start_date) -> State  (task_09)
- log_time(state, req: LogRequest) -> State     (task_08)
- upsert_entry(state, entry: Entry) -> State    (task_08)
- delete_entry(state, day: date) -> State       (task_11)

See tasks/task_08.md, task_09.md, task_11.md. No skeleton implementations — you add these.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, replace
from datetime import date

from progression_bot.domain.models import Entry, State


@dataclass(frozen=True)
class LogRequest:
    """Request to log time for a day (used by task_08 tests and your log handler)."""
    day: date
    minutes: int
    note: str | None = None

def upsert_entry(state: State, entry: Entry) -> State:
    new_entries = []
    replaced = False
    for e in state.entries:
        if e.day == entry.day:
            new_entries.append(entry)
            replaced = True
        else:
            new_entries.append(e)
    if  not replaced:
        new_entries.append(entry)
    new_entries_tuple = tuple(new_entries)
    return dataclasses.replace(state, entries=new_entries_tuple)

def log_time(state: State, req: LogRequest) -> State:
    current = sum(e.minutes for e in state.entries if e.day == req.day)
    new_total = current + req.minutes
    existing_entry = None
    for e in state.entries:
        if e.day == req.day:
            existing_entry = e
            break
    if req.note is not None:
        note = req.note
    else:
        if existing_entry is not None:
            note = existing_entry.note
        else:
            note = None
    new_entry = Entry(day=req.day, minutes=new_total, note=note)
    return upsert_entry(state, new_entry)

def start_progression(state: State, start_date: date) -> State:

    return dataclasses.replace(state, start_date=start_date)