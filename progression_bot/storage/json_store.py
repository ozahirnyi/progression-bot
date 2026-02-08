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
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            state = State(
                version=1,
                tz="UTC",
                schedule=Schedule(
                    workdays=(),
                    daily_target_minutes=0,
                    bonus_threshold_minutes=0,
                ),
                start_date=date.today(),
                plan=Plan(stages=()),
                entries=(),
            )
            self.save(state)
            return state
        else:
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
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data={
            "version": state.version,
            "tz": state.tz,
            "start_date": state.start_date.isoformat(),
            "schedule": {
            "workdays": list(state.schedule.workdays),
            "daily_target": f"{state.schedule.daily_target_minutes//60}h{state.schedule.daily_target_minutes%60}m" if state.schedule.daily_target_minutes>=60 else f"{state.schedule.daily_target_minutes}m",
            "bonus_threshold": f"{state.schedule.bonus_threshold_minutes//60}h{state.schedule.bonus_threshold_minutes%60}m" if state.schedule.bonus_threshold_minutes>=60 else f"{state.schedule.bonus_threshold_minutes}m",
            },
            "plan": {
                "stages": [stage.__dict__ for stage in state.plan.stages],
            },
            "entries": [
                {"date": e.day.isoformat(), "duration": f"{e.minutes//60}h{e.minutes%60}m" if e.minutes>=60 else f"{e.minutes}m", "note": e.note} for e in state.entries
            ],
        }
        tmp_path = self.path.with_suffix(".tmp")
        json_string = json.dumps(data, ensure_ascii=False, indent=2)
        tmp_path.write_text(json_string, encoding="utf-8")
        tmp_path.replace(self.path)

def load_fixture(path: str | Path = "fixtures/mock_state.json") -> State:
    """Convenience helper for loading the fixture."""

    return JsonStore(path=Path(path)).load()

