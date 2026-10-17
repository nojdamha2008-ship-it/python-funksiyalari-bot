#!/usr/bin/env bash
# Linux / macOS uchun tezkor ishga tushirish skripti.
# Ishlatish: ./run.sh   (yoki: bash run.sh)
set -e

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "📦 Virtual muhit (.venv) yaratilmoqda..."
    python3 -m venv .venv
fi

echo "📦 Kutubxonalar o'rnatilmoqda..."
./.venv/bin/pip install --quiet --upgrade pip
./.venv/bin/pip install --quiet -r requirements.txt

if [ ! -f ".env" ]; then
    echo "⚙️  .env fayli topilmadi, .env.example'dan nusxa olinmoqda..."
    cp .env.example .env
    echo "❗ Iltimos, .env faylini oching va BOT_TOKEN qiymatini kiriting, so'ng skriptni qayta ishga tushiring."
    exit 1
fi

echo "🚀 Bot ishga tushirilmoqda..."
./.venv/bin/python bot.py
