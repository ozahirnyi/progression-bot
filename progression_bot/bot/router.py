from __future__ import annotations

from dataclasses import dataclass

from progression_bot.bot.handlers import Handlers


@dataclass(frozen=True)
class Router:
    """Route text commands to handlers.

    This is transport-agnostic: works for CLI demo and can be reused for Telegram
    updates later.
    """

    handlers: Handlers

    def handle(self, text: str) -> str:
        text = text.strip()
        if not text:
            return ""

        if text in {"/start", "start"}:
            return self.handlers.start()
        if text in {"/help", "help"}:
            return self.handlers.help()

        if text.startswith("/status"):
            return self.handlers.status()
        if text.startswith("/heatmap"):
            return self.handlers.heatmap(text=text)
        if text.startswith("/last14"):
            return self.handlers.last14()
        if text.startswith("/plan"):
            return self.handlers.plan()

        # Skeleton: accept /log commands (TODO implementation).
        if text.startswith("/log") or text.startswith("/logy"):
            return self.handlers.log_readonly(text=text)
        if text.startswith("/start_progression"):
            return self.handlers.start_progression_readonly()

        return self.handlers.unknown(text=text)

