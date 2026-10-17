"""
Inline klaviaturalar — jo'natilgan dizayn rasmidagi uslubga mos
(har bir tugma to'liq qatorda, aniq emoji bilan).
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from data.builtins_info import AVAILABLE_LETTERS
from data.lessons import TOTAL_LESSONS


def main_menu_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton("📖 Python Asoslari (Darslar)", callback_data="lesson:0")],
        [InlineKeyboardButton("📚 Barcha Funksiyalar Ro'yxati", callback_data="allfuncs:0")],
        [InlineKeyboardButton("🔤 Harflar bo'yicha Qidiruv", callback_data="letters")],
        [InlineKeyboardButton("🔍 Nom bo'yicha Qidiruv", callback_data="searchprompt")],
        [InlineKeyboardButton("💡 Tasodifiy Funksiya", callback_data="random")],
        [InlineKeyboardButton("✍️ Kod Yozish va Ishga Tushirish", callback_data="codemode:on")],
        [InlineKeyboardButton("⚙️ Yordam & Qo'llanma", callback_data="help")],
    ]
    return InlineKeyboardMarkup(rows)


def back_to_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")]]
    )


def lesson_keyboard(index: int) -> InlineKeyboardMarkup:
    nav_row = []
    if index > 0:
        nav_row.append(InlineKeyboardButton("⬅️ Oldingi", callback_data=f"lesson:{index - 1}"))
    if index < TOTAL_LESSONS - 1:
        nav_row.append(InlineKeyboardButton("Keyingi ➡️", callback_data=f"lesson:{index + 1}"))
    rows = []
    if nav_row:
        rows.append(nav_row)
    rows.append([InlineKeyboardButton(
        f"📑 Darslar ro'yxati ({index + 1}/{TOTAL_LESSONS})", callback_data="lessonslist"
    )])
    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def lessons_list_keyboard() -> InlineKeyboardMarkup:
    from data.lessons import LESSONS

    rows = []
    row = []
    for i, lesson in enumerate(LESSONS):
        row.append(InlineKeyboardButton(f"{i + 1}", callback_data=f"lesson:{i}"))
        if len(row) == 5:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def letters_keyboard() -> InlineKeyboardMarkup:
    rows = []
    row = []
    for letter in AVAILABLE_LETTERS:
        row.append(InlineKeyboardButton(letter, callback_data=f"letter:{letter}"))
        if len(row) == 6:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def functions_page_keyboard(names, page: int, per_page: int, prefix: str) -> InlineKeyboardMarkup:
    start = page * per_page
    chunk = names[start:start + per_page]
    rows = [[InlineKeyboardButton(f"🐍 {n}()", callback_data=f"func:{n}")] for n in chunk]

    nav_row = []
    if page > 0:
        nav_row.append(InlineKeyboardButton("⬅️ Oldingi", callback_data=f"{prefix}:{page - 1}"))
    if start + per_page < len(names):
        nav_row.append(InlineKeyboardButton("Keyingi ➡️", callback_data=f"{prefix}:{page + 1}"))
    if nav_row:
        rows.append(nav_row)

    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def function_card_keyboard(name: str, runnable: bool = True) -> InlineKeyboardMarkup:
    rows = []
    if runnable:
        rows.append([InlineKeyboardButton("▶️ Misolni ishga tushirish", callback_data=f"runexample:{name}")])
    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)


def code_mode_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton("🔚 Kod rejimidan chiqish", callback_data="codemode:off")],
    ]
    return InlineKeyboardMarkup(rows)


def analyzed_function_keyboard(can_run: bool) -> InlineKeyboardMarkup:
    rows = []
    if can_run:
        rows.append([InlineKeyboardButton("▶️ Kodni ishga tushirish", callback_data="runlast")])
    rows.append([InlineKeyboardButton("🔙 Asosiy menyuga qaytish", callback_data="menu")])
    return InlineKeyboardMarkup(rows)
