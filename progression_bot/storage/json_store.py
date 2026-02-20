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
from datetime import datetime, date
from pathlib import Path

from progression_bot.bot.parse import parse_duration_to_minutes
from progression_bot.domain.models import State, Schedule, Plan, PlanStage, Entry

import json

@dataclass(frozen=True)
class JsonStore:
    """Filesystem-backed JSON store."""

    path: Path

    def load(self) -> State:
        with open(self.path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
            stages = []
            entries = []
            workdays = []
            for stage in data["plan"]["stages"]:
                stages.append(PlanStage(**stage))
            for entry in data["entries"]:
                entries.append(Entry(
                    day=datetime.strptime(entry["date"], "%Y-%m-%d").date(),
                    minutes=parse_duration_to_minutes(entry["duration"]),
                    note=entry["note"],
                ))
            for workday in data["schedule"]["workdays"]:
                workdays.append(workday)

            state = State(
                version=int(data["version"]),
                tz=str(data["tz"]),
                schedule=Schedule(
                    workdays=tuple(workdays),
                    daily_target_minutes=parse_duration_to_minutes(data["schedule"]["daily_target"]),
                    bonus_threshold_minutes=parse_duration_to_minutes(data["schedule"]["bonus_threshold"]),
                ),
                start_date=datetime.strptime(data["start_date"], "%Y-%m-%d").date(),
                plan=Plan(stages=tuple(stages)),
                entries=tuple(entries),
            )

        return state

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

