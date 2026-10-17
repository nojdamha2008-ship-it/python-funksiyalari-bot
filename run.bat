@echo off
REM Windows uchun tezkor ishga tushirish skripti.
REM Ishlatish: run.bat (fayl ustiga ikki marta bosing yoki terminalda ishga tushiring)

cd /d "%~dp0"

if not exist ".venv" (
    echo Virtual muhit ^(.venv^) yaratilmoqda...
    python -m venv .venv
)

echo Kutubxonalar o'rnatilmoqda...
.venv\Scripts\pip install --quiet --upgrade pip
.venv\Scripts\pip install --quiet -r requirements.txt

if not exist ".env" (
    echo .env fayli topilmadi, .env.example'dan nusxa olinmoqda...
    copy .env.example .env >nul
    echo Iltimos, .env faylini oching va BOT_TOKEN qiymatini kiriting, so'ng skriptni qayta ishga tushiring.
    pause
    exit /b 1
)

echo Bot ishga tushirilmoqda...
.venv\Scripts\python bot.py
pause
