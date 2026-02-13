from __future__ import annotations

import html
import io
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from progression_bot.bot.heatmap_image import build_heatmap_png
from progression_bot.bot.router import Router
from progression_bot.storage.json_store import JsonStore


@dataclass(frozen=True)
class TelegramBot:
    """Telegram transport adapter.

    Skeleton bot: transport + routing are implemented.
    Business logic is TODO (see tasks/).
    """

    router: Router

    async def _reply_pre(self, update: Update, text: str) -> None:
        if update.message is None:
            return

        for chunk in _split_telegram_message(text):
            await update.message.reply_text(
                text=f"<pre>{html.escape(chunk)}</pre>",
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )

    async def _handle_text(self, update: Update, text: str) -> None:
        parts = text.split()
        if text.startswith("/heatmap"):
            try:
                if len(parts) == 1:
                    weeks = None
                elif len(parts) == 2:
                    weeks = int(parts[1])
                    if weeks <= 0:
                        raise ValueError
                else:
                    raise ValueError
                store = JsonStore(path=Path(self.router.handlers.fixtures_path))
                state = store.load()
                png = build_heatmap_png(state=state, today=date.today(), weeks=weeks)
                if update.message is None:
                    return
                else:
                    buf = io.BytesIO(png)
                    buf.name = "heatmap.png"
                    await update.message.reply_photo(photo=buf)
                return
            except ValueError:
                await self._reply_pre(update, "Usage: /heatmap [weeks]")
                return
        else:
            response = self.router.handle(text)
            await self._reply_pre(update, response)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/start")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/help")

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/status")

    async def plan(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/plan")

    async def last14(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/last14")

    async def heatmap(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        args = " ".join(context.args) if context.args else ""
        text = "/heatmap" if not args else f"/heatmap {args}"
        await self._handle_text(update, text)

    async def log(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        args = " ".join(context.args) if context.args else ""
        text = "/log" if not args else f"/log {args}"
        await self._handle_text(update, text)

    async def logy(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        args = " ".join(context.args) if context.args else ""
        text = "/logy" if not args else f"/logy {args}"
        await self._handle_text(update, text)

    async def start_progression(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await self._handle_text(update, "/start_progression")

    async def unknown_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if update.message is None:
            return
        await self._reply_pre(update, self.router.handle(update.message.text or ""))

    async def non_command_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Treat plain text as unknown command to keep UX clear.
        if update.message is None:
            return
        await self._reply_pre(update, self.router.handle(update.message.text or ""))


def build_application(token: str, router: Router) -> Application:
    bot = TelegramBot(router=router)

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("help", bot.help))
    app.add_handler(CommandHandler("status", bot.status))
    app.add_handler(CommandHandler("plan", bot.plan))
    app.add_handler(CommandHandler("last14", bot.last14))
    app.add_handler(CommandHandler("heatmap", bot.heatmap))
    app.add_handler(CommandHandler("log", bot.log))
    app.add_handler(CommandHandler("logy", bot.logy))
    app.add_handler(CommandHandler("start_progression", bot.start_progression))

    app.add_handler(MessageHandler(filters.COMMAND, bot.unknown_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.non_command_text))
    return app


def _split_telegram_message(text: str, limit: int = 3800) -> list[str]:
    """Split into chunks safe for Telegram (4096 hard limit).

    We also wrap in <pre> tags later, so keep margin.
    """

    if len(text) <= limit:
        return [text]

    chunks: list[str] = []
    buf: list[str] = []
    buf_len = 0

    for line in text.splitlines(keepends=True):
        if len(line) > limit:
            # Fallback: hard split long lines.
            for i in range(0, len(line), limit):
                part = line[i : i + limit]
                if buf:
                    chunks.append("".join(buf).rstrip("\n"))
                    buf, buf_len = [], 0
                chunks.append(part.rstrip("\n"))
            continue

        if buf_len + len(line) > limit and buf:
            chunks.append("".join(buf).rstrip("\n"))
            buf, buf_len = [], 0

        buf.append(line)
        buf_len += len(line)

    if buf:
        chunks.append("".join(buf).rstrip("\n"))
    return chunks

