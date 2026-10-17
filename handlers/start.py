"""/start, /help, /menu, /kod buyruqlari uchun handlerlar."""
from telegram import Update
from telegram.ext import ContextTypes

from config import BANNER_PATH
from utils import texts
from utils.keyboards import back_to_menu_keyboard, code_mode_keyboard, main_menu_keyboard


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["code_mode"] = False
    context.user_data["awaiting_search"] = False

    first_name = update.effective_user.first_name if update.effective_user else "do'stim"
    caption = texts.WELCOME_TEXT.format(first_name=first_name)

    if BANNER_PATH.exists():
        with open(BANNER_PATH, "rb") as photo:
            await update.effective_chat.send_photo(
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=main_menu_keyboard(),
            )
    else:
        await update.effective_chat.send_message(
            caption, parse_mode="HTML", reply_markup=main_menu_keyboard()
        )


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["code_mode"] = False
    context.user_data["awaiting_search"] = False
    await update.effective_chat.send_message(
        "🏠 <b>Bosh menyu</b>\n\nQuyidagi tugmalardan birini tanlang 👇",
        parse_mode="HTML",
        reply_markup=main_menu_keyboard(),
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_chat.send_message(
        texts.HELP_TEXT, parse_mode="HTML", reply_markup=back_to_menu_keyboard()
    )


async def cmd_kod(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["code_mode"] = True
    context.user_data["awaiting_search"] = False
    await update.effective_chat.send_message(
        texts.CODE_MODE_ON_TEXT, parse_mode="HTML", reply_markup=code_mode_keyboard()
    )
