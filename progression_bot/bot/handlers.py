from __future__ import annotations


from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

from progression_bot.storage.json_store import JsonStore
from progression_bot.use_cases.calendar import compute_status


@dataclass(frozen=True)
class Handlers:
    """Command handlers (skeleton).

    Telegram transport stays implemented, but the business logic is TODO.

    Inputs for development:
    - `fixtures/mock_state.json`

    Task spec:
    - `tasks/task_00.md`
    """

    fixtures_path: str = "fixtures/mock_state.json"

    def start(self) -> str:
        return self.help()

    def help(self) -> str:
        return (
            "ProgressionBot (skeleton)\n\n"
            f"Fixture: {self.fixtures_path}\n"
            "Task spec: tasks/task_00.md\n\n"
            "Commands:\n"
            "- /status\n"
            "- /heatmap [weeks]\n"
            "- /last14\n"
            "- /plan\n"
            "- /log <duration>\n"
            "- /log yesterday <duration>\n"
            "- /log YYYY-MM-DD <duration>\n"
            "- /logy <duration>\n"
            "- /start_progression\n"
        )

    def status(self) -> str:
        state = JsonStore(path=Path(self.fixtures_path)).load()
        today = date.today()
        summary = compute_status(state, today)
        done_hours = summary.done_minutes / 60
        total_hours = summary.total_minutes / 60
        remaining_hours = summary.remaining_minutes / 60
        return (
            f"Days to finish: {summary.days_to_finish}\n"
            f"Expected deadline: {summary.expected_deadline_date.isoformat()}\n"
            f"Hours done / total / remaining: "
            f"{done_hours:.1f} / {total_hours:.1f} / {remaining_hours:.1f}"
        )

    def heatmap(self, text: str) -> str:
        return "TODO: implement /heatmap PNG (see tasks/task_06.md)\n"

    def last14(self) -> str:
        return "TODO: implement /last14 (see tasks/task_05.md)\n"

    def plan(self) -> str:
        return "TODO: implement /plan (plan stages)\n"

    def start_progression_readonly(self) -> str:
        return "TODO: implement /start_progression (initialize state)\n"

    def log_readonly(self, text: str) -> str:
        return (
            "TODO: implement /log (time logging)\n\n"
            "Supported examples:\n"
            "- /log 2h\n"
            "- /log 32m\n"
            "- /log 1h30m\n"
            "- /log yesterday 45m\n"
            "- /log 2026-01-23 2h\n"
            "- /logy 1h\n"
        )

    def unknown(self, text: str) -> str:
        return f"Unknown command: {text}\n\nType /help"

