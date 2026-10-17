"""Barcha inline tugma (callback_query) bosishlarini boshqaruvchi handler."""
import random

from telegram import Update
from telegram.ext import ContextTypes

from data.builtins_info import BUILTINS, find_by_name, names_starting_with
from data.lessons import TOTAL_LESSONS, get_lesson
from utils import texts
from utils.formatting import NOT_RUNNABLE_NOTE, esc, format_builtin_card, format_lesson
from utils.keyboards import (
    back_to_menu_keyboard,
    code_mode_keyboard,
    function_card_keyboard,
    functions_page_keyboard,
    lesson_keyboard,
    lessons_list_keyboard,
    letters_keyboard,
    main_menu_keyboard,
)
from utils.sandbox import is_safe, run_code

PER_PAGE = 8


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data or ""
    chat = update.effective_chat

    if data == "menu":
        context.user_data["code_mode"] = False
        context.user_data["awaiting_search"] = False
        await chat.send_message(
            "🏠 <b>Bosh menyu</b>\n\nQuyidagi tugmalardan birini tanlang 👇",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard(),
        )
        return

    if data == "help":
        await chat.send_message(texts.HELP_TEXT, parse_mode="HTML", reply_markup=back_to_menu_keyboard())
        return

    if data == "lessonslist":
        await chat.send_message(
            "📑 <b>Darslar ro'yxati</b>\n\nKerakli dars raqamini tanlang:",
            parse_mode="HTML",
            reply_markup=lessons_list_keyboard(),
        )
        return

    if data.startswith("lesson:"):
        index = int(data.split(":", 1)[1])
        lesson = get_lesson(index)
        if lesson is None:
            await chat.send_message("❌ Dars topilmadi.", reply_markup=main_menu_keyboard())
            return
        await chat.send_message(
            format_lesson(index, lesson, TOTAL_LESSONS),
            parse_mode="HTML",
            reply_markup=lesson_keyboard(index),
        )
        return

    if data == "letters":
        await chat.send_message(
            "🔤 <b>Harflar bo'yicha qidiruv</b>\n\nFunksiya nomi boshlanadigan harfni tanlang:",
            parse_mode="HTML",
            reply_markup=letters_keyboard(),
        )
        return

    if data.startswith("letter:"):
        letter = data.split(":", 1)[1]
        names = names_starting_with(letter)
        if not names:
            await chat.send_message(
                f"❌ '{letter}' harfi bilan boshlanuvchi funksiya topilmadi.",
                reply_markup=letters_keyboard(),
            )
            return
        await chat.send_message(
            f"🔤 <b>'{letter}' harfi bilan boshlanuvchi funksiyalar</b> ({len(names)} ta):",
            parse_mode="HTML",
            reply_markup=functions_page_keyboard(names, 0, PER_PAGE, f"letterfuncs:{letter}"),
        )
        return

    if data.startswith("letterfuncs:"):
        _, letter, page_str = data.split(":")
        page = int(page_str)
        names = names_starting_with(letter)
        await chat.send_message(
            f"🔤 <b>'{letter}' harfi bilan boshlanuvchi funksiyalar</b> ({len(names)} ta):",
            parse_mode="HTML",
            reply_markup=functions_page_keyboard(names, page, PER_PAGE, f"letterfuncs:{letter}"),
        )
        return

    if data.startswith("allfuncs:"):
        page = int(data.split(":", 1)[1])
        names = sorted(BUILTINS.keys())
        await chat.send_message(
            f"📚 <b>Barcha funksiyalar</b> ({len(names)} ta):",
            parse_mode="HTML",
            reply_markup=functions_page_keyboard(names, page, PER_PAGE, "allfuncs"),
        )
        return

    if data == "searchprompt":
        context.user_data["awaiting_search"] = True
        await chat.send_message(texts.SEARCH_PROMPT_TEXT, parse_mode="HTML")
        return

    if data == "random":
        name = random.choice(list(BUILTINS.keys()))
        info = BUILTINS[name]
        runnable = is_safe(info["example"])
        card_text = format_builtin_card(name, info) + ("" if runnable else NOT_RUNNABLE_NOTE)
        await chat.send_message(
            card_text,
            parse_mode="HTML",
            reply_markup=function_card_keyboard(name, runnable=runnable),
        )
        return

    if data.startswith("func:"):
        name = data.split(":", 1)[1]
        info = find_by_name(name)
        if not info:
            await chat.send_message(
                texts.NOT_FOUND_TEXT.format(query=esc(name)),
                parse_mode="HTML",
                reply_markup=main_menu_keyboard(),
            )
            return
        runnable = is_safe(info["example"])
        card_text = format_builtin_card(name, info) + ("" if runnable else NOT_RUNNABLE_NOTE)
        await chat.send_message(
            card_text,
            parse_mode="HTML",
            reply_markup=function_card_keyboard(name, runnable=runnable),
        )
        return

    if data.startswith("runexample:"):
        name = data.split(":", 1)[1]
        info = find_by_name(name)
        if not info:
            await chat.send_message("❌ Misol topilmadi.", reply_markup=main_menu_keyboard())
            return
        await chat.send_message("⏳ Kod ishga tushirilmoqda...")
        result = run_code(info["example"])
        await _send_run_result(chat, result)
        return

    if data == "runlast":
        code = context.user_data.get("last_code")
        if not code:
            await chat.send_message(
                "❌ Ishga tushirish uchun oldin kod yuboring.", reply_markup=main_menu_keyboard()
            )
            return
        await chat.send_message("⏳ Kod ishga tushirilmoqda...")
        result = run_code(code)
        await _send_run_result(chat, result)
        return

    if data.startswith("codemode:"):
        state = data.split(":", 1)[1]
        if state == "on":
            context.user_data["code_mode"] = True
            await chat.send_message(
                texts.CODE_MODE_ON_TEXT, parse_mode="HTML", reply_markup=code_mode_keyboard()
            )
        else:
            context.user_data["code_mode"] = False
            await chat.send_message(
                texts.CODE_MODE_OFF_TEXT, reply_markup=main_menu_keyboard()
            )
        return

    # Noma'lum callback - xato bermasdan bosh menyuga qaytaramiz
    await chat.send_message(
        "🏠 Bosh menyu:", reply_markup=main_menu_keyboard()
    )


async def _send_run_result(chat, result) -> None:
    if result.ok:
        text = f"✅ <b>Natija:</b>\n<code>{esc(result.output)}</code>"
    else:
        text = f"❌ <b>Xatolik:</b>\n<code>{esc(result.error)}</code>"
        if result.output:
            text += f"\n\n<b>Chiqish (stdout):</b>\n<code>{esc(result.output)}</code>"
    await chat.send_message(text, parse_mode="HTML", reply_markup=main_menu_keyboard())
