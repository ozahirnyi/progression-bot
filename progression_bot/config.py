from __future__ import annotations

from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    """Runtime configuration.

    Note: in the current stage we run a read-only CLI demo by default.
    Telegram wiring can be added later using BOT_TOKEN.
    """

    bot_token: str | None
    tz: str
    storage_path: str
    demo_mode: bool


def load_config() -> Config:
    """Load configuration from environment variables.

    Env:
    - BOT_TOKEN: Telegram bot token (optional for demo)
    - TZ: timezone name (e.g. Europe/Kyiv)
    - STORAGE_PATH: path to JSON state (unused in demo)
    - DEMO_MODE: if '1', forces demo mode
    """

    # Load .env if present (never commit secrets).
    load_dotenv(override=False)

    bot_token = getenv("BOT_TOKEN")
    tz = getenv("TZ", "Europe/Kyiv")
    storage_path = getenv("STORAGE_PATH", "./data/state.json")
    demo_mode = getenv("DEMO_MODE", "").strip() in {"1", "true", "True", "yes", "YES"}
    return Config(bot_token=bot_token, tz=tz, storage_path=storage_path, demo_mode=demo_mode)

