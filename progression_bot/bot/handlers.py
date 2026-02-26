from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

from progression_bot.bot.parse import parse_log_command
from progression_bot.storage.json_store import JsonStore
from progression_bot.use_cases.calendar import compute_status, last_n_days
from progression_bot.use_cases.progress import log_time
from progression_bot.use_cases.progress import start_progression

@dataclass(frozen=True)
class Handlers:
    """Command handlers (skeleton).

    Telegram transport stays implemented, but the business logic is TODO.

    Inputs for development:
    - `fixtures/mock_state.json`

    Task spec:
    - `tasks/task_00.md`
    """

    fixtures_path: str

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
        state = JsonStore(path=Path(self.fixtures_path)).load()
        today = date.today()
        days = last_n_days(state, today, 14)
        lines = []
        lines.append("Last 14 days:")
        for day_info in days:
            day_str = day_info.day.isoformat()
            weekday = day_info.day.strftime("%a")
            minutes = day_info.minutes
            if minutes < 60:
                duration = f"{minutes}m"
            else:
                duration = f"{minutes // 60}h{minutes % 60}m"
            line = f"{day_str} {weekday} {duration} {day_info.status}"
            if day_info.note:
                line += f" {day_info.note}"
            lines.append(line)
        return "\n".join(lines)

    def plan(self) -> str:
        return "TODO: implement /plan (plan stages)\n"

    def start_progression(self, text: str) -> str:
        parts = text.split()
        try:
            if len(parts) == 1:
                day = date.today()
            elif len(parts) == 2:
                day = date.fromisoformat(parts[1])
            else:
                return "Usage: /start_progression <day>"
        except ValueError:
            return "Usage: /start_progression <day>"
        store = JsonStore(path=Path(self.fixtures_path))
        state = store.load()
        new_state = start_progression(state, day)
        store.save(new_state)
        return f"Start date set to {day.isoformat()}"

    def log(self, text: str) -> str:
        store = JsonStore(Path(self.storage_path))
        state = store.load()
        try:
            req = parse_log_command(text)
            new_state = log_time(state, req)
            store.save(new_state)
            return f"Logged {req.minutes}m for {req.day}"
        except (ValueError, TypeError):
            return "Usage: /log 2h or /log yesterday 45m"

    def unknown(self, text: str) -> str:
        return f"Unknown command: {text}\n\nType /help"

