from __future__ import annotations

import argparse
import os

from progression_bot.bot.router import Router
from progression_bot.bot.telegram_app import build_application
from progression_bot.bot.handlers import Handlers
from progression_bot.config import load_config


WELCOME = """ProgressionBot (skeleton)

Type a command and press Enter.
Examples:
  /help
  /status
  /heatmap
  /last14
  /plan
  /log 2h
  /log yesterday 32m

Type /quit to exit.

See tasks:
  tasks/task_00.md
"""


def main() -> int:
    parser = argparse.ArgumentParser(prog="progression_bot")
    parser.add_argument("--cli", action="store_true", help="Run local CLI demo even if BOT_TOKEN is set")
    args = parser.parse_args()

    cfg = load_config()

    handlers = Handlers(fixtures_path=cfg.storage_path)
    router = Router(handlers=handlers)

    if cfg.bot_token and not args.cli:
        # Telegram transport mode.
        os.environ["FORCE_EMOJI"] = "1"
        app = build_application(token=cfg.bot_token, router=router)
        app.run_polling(close_loop=False)
        return 0

    # CLI mode (no Telegram).
    print(WELCOME)
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not raw:
            continue
        if raw in {"/quit", "quit", "exit"}:
            return 0

        print(router.handle(raw))


if __name__ == "__main__":
    raise SystemExit(main())

