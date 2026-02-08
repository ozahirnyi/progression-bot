"""Telegram command parsing (student-owned).

This module should parse user input into structured data that use-cases can use.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta, datetime



@dataclass(frozen=True)
class LogCommand:
    """Normalized /log command."""

    day: date
    minutes: int
    note: str | None = None


def parse_duration_to_minutes(raw: str) -> int:
    raw = raw.strip()
    minutes_total = 0
    if "h" in raw:
        hours_str = raw.split("h")[0].strip()
        minutes_total += int(float(hours_str) * 60)
        raw = raw.split("h", 1)[1]
    if "m" in raw:
        minutes_str = raw.split("m")[0].strip()
        minutes_total += int(minutes_str)
        raw = raw.split("m", 1)[1]
    if raw.strip():
        raise ValueError("Invalid format")
    if minutes_total <= 0:
        raise ValueError("Minutes must be > 0")
    return minutes_total


def parse_log_command(text: str, today: date) -> LogCommand:
    parts = text.split()
    if parts[0] == "/logy":
        day = today - timedelta(days=1)
        if len(parts) < 2:
            raise ValueError("Duration is missing")
        duration_str = parts[1]
    elif parts[0] == "/log":
        if len(parts) > 1 and parts[1] == "yesterday":
            day = today - timedelta(days=1)
            if len(parts) < 3:
                raise ValueError("Duration is missing")
            duration_str = parts[2]
        else:
            try:
                day = datetime.strptime(parts[1], "%Y-%m-%d").date()
                if len(parts) < 3:
                    raise ValueError("Duration is missing")
                duration_str = parts[2]
            except (ValueError, IndexError):
                day = today
                if len(parts) < 2:
                    raise ValueError("Duration is missing")
                duration_str = parts[1]
    else:
        raise ValueError("Unknown command")

    minutes = parse_duration_to_minutes(duration_str)

    return LogCommand(day=day, minutes=minutes, note=None)

