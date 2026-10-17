"""
Foydalanuvchi yuborgan Python kodini xavfsiz (sandbox) muhitda ishga
tushirish uchun vositalar.

Xavfsizlik choralari:
  - Kod alohida subprocess'da, asosiy bot jarayonidan ajratilgan holda ishga tushadi.
  - Xavfli modullar/funksiyalar (os, sys, subprocess, socket, ...) AST orqali oldindan taqiqlanadi.
  - CPU vaqti va operativ xotira resurslari cheklanadi (Unix tizimlarida).
  - Ishga tushirish vaqti timeout bilan chegaralanadi.
  - Chiqish natijasi belgilangan uzunlikdan oshsa, qisqartiriladi.
"""
from __future__ import annotations

import ast
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from config import CODE_MAX_MEMORY_MB, CODE_MAX_OUTPUT_CHARS, CODE_TIMEOUT_SECONDS

# Taqiqlangan modul nomlari (xavfsizlik uchun)
FORBIDDEN_MODULES = {
    "os", "sys", "subprocess", "shutil", "socket", "importlib",
    "ctypes", "multiprocessing", "threading", "signal", "resource",
    "pty", "pdb", "sysconfig", "platform", "pathlib", "glob",
    "http", "urllib", "ftplib", "telnetlib", "smtplib", "pickle",
}

# Taqiqlangan funksiya/nomlar
FORBIDDEN_NAMES = {
    "eval", "exec", "compile", "__import__", "open", "input",
    "exit", "quit", "globals", "locals", "vars", "breakpoint",
    "memoryview", "help",
}


@dataclass
class RunResult:
    ok: bool
    output: str
    error: str | None = None


def _check_safety(code: str) -> str | None:
    """Kodni AST orqali tekshiradi. Xavfli bo'lsa, xato matnini qaytaradi, aks holda None."""
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return f"Sintaksis xatosi: {exc.msg} (qator {exc.lineno})"

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name.split(".")[0] for alias in node.names]
            else:
                if node.module:
                    names = [node.module.split(".")[0]]
            for name in names:
                if name in FORBIDDEN_MODULES:
                    return (
                        f"🚫 Xavfsizlik sababli '{name}' modulini import qilib bo'lmaydi.\n"
                        "Bu bot faqat asosiy Python kodini (o'zgaruvchilar, sikllar, "
                        "funksiyalar, ro'yxatlar va h.k.) ishga tushiradi."
                    )
        if isinstance(node, ast.Name) and node.id in FORBIDDEN_NAMES:
            return (
                f"🚫 Xavfsizlik sababli '{node.id}()' funksiyasidan foydalanib bo'lmaydi."
            )
        if isinstance(node, ast.Attribute) and node.attr in {"system", "popen", "remove", "rmdir", "unlink"}:
            return "🚫 Xavfsizlik sababli fayl/tizim buyruqlaridan foydalanib bo'lmaydi."

    return None


def _limit_resources():  # pragma: no cover - faqat Unix tizimlarida ishlaydi
    try:
        import resource

        mem_bytes = CODE_MAX_MEMORY_MB * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
        # CPU limitni subprocess.run() timeout'idan biroz kattaroq qilamiz - shunda
        # avval "toza" timeout ishlaydi va aniq, tushunarli xabar chiqadi.
        cpu_limit = CODE_TIMEOUT_SECONDS + 2
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit))
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
        resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    except Exception:
        pass


def run_code(code: str) -> RunResult:
    """Berilgan Python kodini xavfsiz sandbox ichida ishga tushiradi."""
    safety_issue = _check_safety(code)
    if safety_issue:
        return RunResult(ok=False, output="", error=safety_issue)

    with tempfile.TemporaryDirectory(prefix="pybot_sandbox_") as tmpdir:
        script_path = Path(tmpdir) / "user_code.py"
        script_path.write_text(code, encoding="utf-8")

        popen_kwargs = dict(
            args=[sys.executable, "-I", str(script_path)],
            cwd=tmpdir,
            capture_output=True,
            text=True,
            timeout=CODE_TIMEOUT_SECONDS,
        )
        if sys.platform != "win32":
            popen_kwargs["preexec_fn"] = _limit_resources

        try:
            proc = subprocess.run(**popen_kwargs)
        except subprocess.TimeoutExpired:
            return RunResult(
                ok=False,
                output="",
                error=f"⏱ Kod {CODE_TIMEOUT_SECONDS} soniyadan ko'proq vaqt oldi va to'xtatildi "
                      "(cheksiz sikl bo'lishi mumkin).",
            )
        except Exception as exc:  # noqa: BLE001
            return RunResult(ok=False, output="", error=f"Ishga tushirishda xatolik: {exc}")

        stdout = proc.stdout or ""
        stderr = proc.stderr or ""

        if len(stdout) > CODE_MAX_OUTPUT_CHARS:
            stdout = stdout[:CODE_MAX_OUTPUT_CHARS] + "\n... (natija qisqartirildi)"
        if len(stderr) > CODE_MAX_OUTPUT_CHARS:
            stderr = stderr[:CODE_MAX_OUTPUT_CHARS] + "\n... (xatolik matni qisqartirildi)"

        if proc.returncode != 0:
            if not stderr and proc.returncode < 0:
                stderr = (
                    "⏱ Kod resurs chegarasidan oshib ketdi (juda ko'p vaqt yoki "
                    "xotira ishlatdi) va majburan to'xtatildi."
                )
            return RunResult(ok=False, output=stdout, error=stderr or "Noma'lum xatolik yuz berdi.")

        return RunResult(ok=True, output=stdout or "(dastur hech narsa chiqarmadi)", error=None)


def is_safe(code: str) -> bool:
    """Kod xavfsizlik tekshiruvidan (import/nom taqiqlari) o'tishini bildiradi."""
    return _check_safety(code) is None
