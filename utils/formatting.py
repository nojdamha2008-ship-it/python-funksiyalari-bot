"""Matnni Telegram HTML parse_mode uchun xavfsiz tayyorlash yordamchisi."""
import html


def esc(text: str) -> str:
    """&, <, > belgilarini HTML uchun xavfsiz shaklga o'tkazadi (tirnoqlarga tegmaydi)."""
    return html.escape(str(text), quote=False)


NOT_RUNNABLE_NOTE = (
    "\n\nℹ️ <i>Bu funksiyani xavfsizlik uchun shu yerda jonli ishga tushirib "
    "bo'lmaydi (interaktiv yoki fayl/tizim funksiyasi), lekin misolni o'qib "
    "tushunishingiz mumkin.</i>"
)


def format_builtin_card(name: str, info: dict) -> str:
    """Bosh dizayn rasmidagi 'Maqsadi / Sintaksis / Parametrlar / Misol' kartochka formati."""
    lines = [
        f"📄 <b>{esc(name)}() funktsiyasi</b> 🐍",
        "",
        f"<b>Maqsadi:</b> {esc(info['purpose'])}",
        "",
        "<b>Sintaksis:</b>",
        f"<code>{esc(info['syntax'])}</code>",
        "",
        "<b>Parametrlar:</b>",
    ]
    if info["params"]:
        for pname, pdesc in info["params"]:
            lines.append(f"- <b>{esc(pname)}</b>: {esc(pdesc)}")
    else:
        lines.append("- yo'q")

    lines += ["", "<b>Misol:</b>", f"<code>{esc(info['example'])}</code>"]
    return "\n".join(lines)


def format_lesson(index: int, lesson: dict, total: int) -> str:
    lines = [
        f"{lesson['emoji']} <b>{index + 1}-dars: {esc(lesson['title'])}</b>  ({index + 1}/{total})",
        "",
        lesson["content"],
    ]
    if lesson.get("example"):
        lines += ["", "<b>Misol kod:</b>", f"<code>{esc(lesson['example'])}</code>"]
    return "\n".join(lines)
