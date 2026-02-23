"""Domain models (student-owned).

This module defines the *data shapes* used by the bot logic.

Important:
- Keep this module independent from Telegram / files / IO.
- Prefer plain dataclasses + simple types.
- Store time as **minutes (int)** internally.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal


Weekday = Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


@dataclass(frozen=True)
class Schedule:
    """Weekly schedule rules."""

    workdays: tuple[Weekday, ...]  # typically Mon..Fri
    daily_target_minutes: int  # 2h -> 120
    bonus_threshold_minutes: int  # 3h -> 180


@dataclass(frozen=True)
class PlanStage:
    name: str
    expected_hours: int


@dataclass(frozen=True)
class Plan:
    stages: tuple[PlanStage, ...]

    def total_planned_minutes(self) -> int:
        total = 0
        for stage in self.stages:
            total += stage.expected_hours * 60
        return total



@dataclass(frozen=True)
class Entry:
    """One day of progress."""

    day: date
    minutes: int
    note: str | None = None


@dataclass(frozen=True)
class State:
    """Full bot state (single-user)."""

    version: int
    tz: str
    schedule: Schedule
    start_date: date | None
    plan: Plan
    entries: tuple[Entry, ...]


@dataclass(frozen=True)
class StatusSummary:
    """Computed /status output values."""

    total_minutes: int
    done_minutes: int
    remaining_minutes: int
    expected_deadline_date: date
    days_to_finish: int


DayStatus = Literal["empty", "weekend", "missed", "partial", "done", "bonus", "today"]


@dataclass(frozen=True)
class DayInfo:
    """A single day as shown in /last14 or heatmap."""

    day: date
    minutes: int
    status: DayStatus
    note: str | None = None

