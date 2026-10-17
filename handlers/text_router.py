"""
Oddiy matn xabarlarini (buyruq bo'lmagan) boshqaruvchi handler.

Uch xil holatni qayta ishlaydi:
  1. Kod yozish rejimi yoqilgan bo'lsa -> kodni sandboxda ishga tushiradi.
  2. "Nom bo'yicha qidiruv" so'ralgan bo'lsa -> built-in funksiyani qidiradi.
  3. Aks holda -> xabarda 'def funksiya(...)' bo'lsa avtomatik tahlil qiladi,
     yoki built-in funksiya nomiga to'g'ridan-to'g'ri mos kelsa ma'lumot beradi,
     hech biriga mos kelmasa - yordamchi (fallback) xabar yuboradi.
"""
from telegram import Update
from telegram.ext import ContextTypes

from data.builtins_info import find_by_name
from utils import texts
from utils.analyzer import extract_functions, format_function_card, looks_like_python_code
from utils.formatting import NOT_RUNNABLE_NOTE, esc, format_builtin_card
from utils.keyboards import (
    analyzed_function_keyboard,
    code_mode_keyboard,
    function_card_keyboard,
    main_menu_keyboard,
)
from utils.sandbox import is_safe, run_code

MAX_FUNCTIONS_SHOWN = 3


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if not message or not message.text:
        return
    text = message.text
    chat = update.effective_chat

    if context.user_data.get("code_mode"):
        await _handle_code_submission(chat, context, text)
        return

    if context.user_data.get("awaiting_search"):
        context.user_data["awaiting_search"] = False
        await _handle_search(chat, text)
        return

    if "def " in text and looks_like_python_code(text):
        await _handle_function_analysis(chat, context, text)
        return

    info = find_by_name(text)
    if info:
        name = text.strip().lower().replace("()", "").split("(")[0]
        runnable = is_safe(info["example"])
        card_text = format_builtin_card(name, info) + ("" if runnable else NOT_RUNNABLE_NOTE)
        await chat.send_message(
            card_text,
            parse_mode="HTML",
            reply_markup=function_card_keyboard(name, runnable=runnable),
        )
        return

    await chat.send_message(texts.FALLBACK_TEXT, parse_mode="HTML", reply_markup=main_menu_keyboard())


async def _handle_search(chat, query_text: str) -> None:
    info = find_by_name(query_text)
    if not info:
        await chat.send_message(
            texts.NOT_FOUND_TEXT.format(query=esc(query_text.strip())),
            parse_mode="HTML",
            reply_markup=main_menu_keyboard(),
        )
        return
    name = query_text.strip().lower().replace("()", "").split("(")[0]
    runnable = is_safe(info["example"])
    card_text = format_builtin_card(name, info) + ("" if runnable else NOT_RUNNABLE_NOTE)
    await chat.send_message(
        card_text,
        parse_mode="HTML",
        reply_markup=function_card_keyboard(name, runnable=runnable),
    )


async def _handle_function_analysis(chat, context, code_text: str) -> None:
    functions = extract_functions(code_text)
    context.user_data["last_code"] = code_text

    if not functions:
        await chat.send_message(
            "⚠️ Kodda 'def' so'zi bor, lekin funksiyani tahlil qilib bo'lmadi "
            "(sintaksis xato bo'lishi mumkin). Kodingizni tekshirib qayta yuboring.",
            reply_markup=main_menu_keyboard(),
        )
        return

    for info in functions[:MAX_FUNCTIONS_SHOWN]:
        await chat.send_message(
            format_function_card(info),
            parse_mode="HTML",
            reply_markup=analyzed_function_keyboard(can_run=True),
        )

    if len(functions) > MAX_FUNCTIONS_SHOWN:
        await chat.send_message(
            f"ℹ️ Kodda yana {len(functions) - MAX_FUNCTIONS_SHOWN} ta funksiya bor, "
            "lekin faqat birinchi 3 tasi ko'rsatildi."
        )


async def _handle_code_submission(chat, context, code_text: str) -> None:
    context.user_data["last_code"] = code_text

    functions = extract_functions(code_text)
    for info in functions[:MAX_FUNCTIONS_SHOWN]:
        await chat.send_message(format_function_card(info), parse_mode="HTML")

    await chat.send_message("⏳ Kod ishga tushirilmoqda...")
    result = run_code(code_text)

    if result.ok:
        text = f"✅ <b>Natija:</b>\n<code>{esc(result.output)}</code>"
    else:
        text = f"❌ <b>Xatolik:</b>\n<code>{esc(result.error)}</code>"
        if result.output:
            text += f"\n\n<b>Chiqish (stdout):</b>\n<code>{esc(result.output)}</code>"

    await chat.send_message(
        text + "\n\n✍️ Yana kod yuborishingiz mumkin.",
        parse_mode="HTML",
        reply_markup=code_mode_keyboard(),
    )
