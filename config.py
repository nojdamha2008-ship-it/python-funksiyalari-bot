"""
Bot konfiguratsiyasi.
.env faylidan sozlamalarni o'qiydi.
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

BANNER_PATH = BASE_DIR / "assets" / "banner.jpg"

# Kod ishga tushirish (sandbox) sozlamalari
CODE_TIMEOUT_SECONDS = 5
CODE_MAX_OUTPUT_CHARS = 3500
CODE_MAX_MEMORY_MB = 64

BOT_NAME = "Python Funktsiyalari Boti"


def check_token() -> None:
    """Token mavjudligini tekshiradi, aks holda tushunarli xato bilan to'xtaydi."""
    if not BOT_TOKEN:
        print(
            "\n❌ XATOLIK: BOT_TOKEN topilmadi!\n\n"
            "1) '.env.example' faylidan nusxa oling: cp .env.example .env\n"
            "2) '.env' faylini oching va @BotFather dan olingan tokenni kiriting.\n"
            "3) Botni qayta ishga tushiring: python bot.py\n",
            file=sys.stderr,
        )
        sys.exit(1)
