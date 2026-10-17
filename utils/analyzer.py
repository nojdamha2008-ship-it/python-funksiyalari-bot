"""
Foydalanuvchi yuborgan Python kodidagi funksiya(lar)ni AST yordamida
tahlil qilib, ular haqida tushunarli ma'lumot chiqaradi
(dizayn rasmidagi funksiya-kartochka uslubida).
"""
from __future__ import annotations

import ast
from dataclasses import dataclass, field


@dataclass
class FunctionInfo:
    name: str
    args: list[str]
    defaults: dict
    docstring: str | None
    has_return: bool
    line_count: int
    calls: list[str] = field(default_factory=list)


def looks_like_python_code(text: str) -> bool:
    """Matn Python kodi bo'lishi mumkinligini tez tekshiradi."""
    stripped = text.strip()
    if not stripped:
        return False
    markers = ("def ", "class ", "import ", "for ", "while ", "print(", "if ", "return ")
    if any(marker in stripped for marker in markers):
        try:
            ast.parse(stripped)
            return True
        except SyntaxError:
            return False
    return False


def extract_functions(code: str) -> list[FunctionInfo]:
    """Koddagi barcha 'def' orqali yozilgan funksiyalarni tahlil qiladi."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    results = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [a.arg for a in node.args.args]

            defaults = {}
            defaults_list = node.args.defaults
            if defaults_list:
                paired_args = args[-len(defaults_list):]
                for name, default_node in zip(paired_args, defaults_list):
                    try:
                        defaults[name] = ast.literal_eval(default_node)
                    except Exception:
                        defaults[name] = "..."

            docstring = ast.get_docstring(node)

            has_return = any(
                isinstance(n, ast.Return) and n.value is not None
                for n in ast.walk(node)
            )

            calls = sorted({
                n.func.id
                for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            })

            line_count = (node.end_lineno or node.lineno) - node.lineno + 1

            results.append(
                FunctionInfo(
                    name=node.name,
                    args=args,
                    defaults=defaults,
                    docstring=docstring,
                    has_return=has_return,
                    line_count=line_count,
                    calls=calls,
                )
            )
    return results


def format_function_card(info: FunctionInfo) -> str:
    """FunctionInfo'ni dizayndagi 'Maqsadi / Sintaksis / Parametrlar' formatida chiqaradi."""
    args_display = []
    for a in info.args:
        if a in info.defaults:
            args_display.append(f"{a}={info.defaults[a]!r}")
        else:
            args_display.append(a)
    syntax = f"{info.name}({', '.join(args_display)})"

    if info.docstring:
        purpose = info.docstring.strip().splitlines()[0]
    elif info.has_return:
        purpose = "Hisoblash/qayta ishlash bajarib, natija (return) qaytaradi."
    else:
        purpose = "Amal bajaradi (return orqali natija qaytarmaydi)."

    lines = [
        f"📄 <b>{info.name}() funksiyasi</b> 🐍  <i>(sizning kodingiz)</i>",
        "",
        f"<b>Maqsadi:</b> {purpose}",
        "",
        "<b>Sintaksis:</b>",
        f"<code>{syntax}</code>",
    ]

    if info.args:
        lines.append("")
        lines.append("<b>Parametrlar:</b>")
        for a in info.args:
            default_note = f" (standart: {info.defaults[a]!r})" if a in info.defaults else ""
            lines.append(f"- <b>{a}</b>{default_note}")
    else:
        lines.append("")
        lines.append("<b>Parametrlar:</b> yo'q")

    return_note = "Ha (return bor)" if info.has_return else "Yo'q"
    lines.append("")
    lines.append(f"<b>Kod uzunligi:</b> {info.line_count} qator")
    lines.append(f"<b>Natija qaytaradimi:</b> {return_note}")

    if info.calls:
        lines.append(f"<b>Ichida chaqirilgan funksiyalar:</b> {', '.join(info.calls)}")

    return "\n".join(lines)
