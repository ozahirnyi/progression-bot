"""Telegram command parsing (student-owned).

This module should parse user input into structured data that use-cases can use.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class LogCommand:
    """Normalized /log command."""

    day: date
    minutes: int
    note: str | None = None


def parse_duration_to_minutes(raw: str) -> int:
    """Parse '32m', '2h', '1h30m', '2h 15m', '2.5h' into minutes.

    TODO(student): Implement.
    """

    raise NotImplementedError


def parse_log_command(text: str, today: date) -> LogCommand:
    """Parse raw command text like:
    - '/log 2h'
    - '/log yesterday 45m'
    - '/log 2026-01-23 2.5h'
    - '/logy 1h'

    TODO(student): Implement.
    """

    raise NotImplementedError

