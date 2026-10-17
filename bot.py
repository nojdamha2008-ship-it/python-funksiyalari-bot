#!/usr/bin/env python3
"""
Python Funktsiyalari Boti — asosiy ishga tushirish fayli.

Ishga tushirish:
    python bot.py

Talablar:
    1) pip install -r requirements.txt
    2) .env faylida BOT_TOKEN ko'rsatilgan bo'lishi kerak (.env.example'ga qarang)
"""
import logging

from telegram import Update
from telegram.error import TelegramError
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import config
from handlers.callbacks import on_callback
from handlers.start import cmd_help, cmd_kod, cmd_menu, cmd_start
from handlers.text_router import on_text

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger("python_funksiyalar_boti")


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Har qanday kutilmagan xatolikni ushlab, dastur to'xtab qolishining oldini oladi."""
    logger.exception("Xatolik yuz berdi", exc_info=context.error)

    if isinstance(update, Update) and update.effective_chat:
        try:
            await update.effective_chat.send_message(
                "⚠️ Kutilmagan xatolik yuz berdi. Iltimos, /start buyrug'ini qayta yuboring."
            )
        except TelegramError:
            pass


def build_application() -> Application:
    application = Application.builder().token(config.BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(CommandHandler("menu", cmd_menu))
    application.add_handler(CommandHandler("help", cmd_help))
    application.add_handler(CommandHandler("kod", cmd_kod))

    application.add_handler(CallbackQueryHandler(on_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))

    application.add_error_handler(on_error)
    return application


def main() -> None:
    config.check_token()
    application = build_application()

    print(f"\n🐍 {config.BOT_NAME} ishga tushdi! To'xtatish uchun Ctrl+C bosing.\n")
    logger.info("Bot polling rejimida ishga tushdi.")

    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
