# 🐍 Python Funktsiyalari Boti

Python asoslarini bosqichma-bosqich o'rgatadigan, har qanday built-in yoki
o'zingiz yozgan funksiya haqida ma'lumot beradigan, va kodingizni to'g'ridan-to'g'ri
Telegram ichida yozib, ishga tushirib ko'rish imkonini beruvchi Telegram bot.

## ✨ Imkoniyatlar

- **📖 Python asoslari** — o'zgaruvchilardan tortib OOP'gacha 19 ta qisqa, tushunarli dars.
- **🔍 Funksiyalar ma'lumotnomasi** — 35+ built-in funksiya (`print`, `len`, `range`, `sorted` va h.k.) haqida to'liq ma'lumot: maqsadi, sintaksisi, parametrlari va misoli.
- **🔤 Harflar / 🔍 Nom bo'yicha qidiruv** va **💡 Tasodifiy funksiya** — qulay navigatsiya.
- **🧩 Avtomatik funksiya tahlili** — botga o'zingiz yozgan `def funksiya(...):` kodini yuborsangiz, bot uni tahlil qilib, parametrlari va vazifasi haqida ma'lumot beradi.
- **✍️ Kod yozish va ishga tushirish rejimi** — "Kod yozish" tugmasini bosib, istalgan Python kodini yuboring — bot uni xavfsiz (sandbox) muhitda ishga tushirib, natijasini qaytaradi.
- **🔒 Xavfsiz kod ishga tushirish** — `os`, `sys`, `subprocess` kabi tizim modullari taqiqlangan, ishga tushirish vaqti va xotira resurslari cheklangan, kod alohida jarayonda (subprocess) ishlaydi.

## 📁 Loyiha tuzilishi

```
python_funksiyalar_boti/
├── bot.py                  # Botni ishga tushiruvchi asosiy fayl
├── config.py                # .env sozlamalarini o'qiydi
├── requirements.txt          # Kerakli kutubxonalar
├── .env.example               # BOT_TOKEN namunasi (nusxa ko'chirib .env qiling)
├── run.sh / run.bat            # Bir bosishda o'rnatib, ishga tushiruvchi skriptlar
├── data/
│   ├── builtins_info.py         # Built-in funksiyalar ma'lumotlar bazasi
│   └── lessons.py                # Python asoslari darslari
├── handlers/
│   ├── start.py                   # /start /menu /help /kod buyruqlari
│   ├── callbacks.py                # Barcha inline tugmalarni boshqaradi
│   └── text_router.py               # Oddiy matn xabarlarini boshqaradi
├── utils/
│   ├── keyboards.py                  # Inline klaviaturalar
│   ├── formatting.py                  # Xabar matnlarini formatlash (HTML)
│   ├── texts.py                        # Statik matnlar
│   ├── analyzer.py                      # Foydalanuvchi kodidagi funksiyani AST orqali tahlil qilish
│   └── sandbox.py                        # Kodni xavfsiz ishga tushirish (sandbox)
└── assets/
    └── banner.jpg                          # /start xabaridagi rasm
```

## 🚀 O'rnatish va ishga tushirish

### 1-qadam — Telegram bot yaratish

1. Telegram'da [@BotFather](https://t.me/BotFather) botiga o'ting.
2. `/newbot` buyrug'ini yuboring va ko'rsatmalarga amal qiling (bot nomi va username so'raladi).
3. BotFather sizga quyidagiga o'xshash **token** beradi:
   `123456789:AAExampleTokenHereXXXXXXXXXXXXXXXXX`
4. Ushbu tokenni saqlab qo'ying — u sizning shaxsiy kalitingiz, hech kimga bermang.

### 2-qadam — Loyihani tayyorlash

Terminal (Linux/macOS) yoki Buyruqlar satri / PowerShell (Windows) oching va
`python_funksiyalar_boti` papkasi ichiga kiring:

```bash
cd python_funksiyalar_boti
```

**Talab:** kompyuterda Python 3.10 yoki undan yuqori versiya o'rnatilgan bo'lishi kerak.
Tekshirish uchun:

```bash
python3 --version
```

### 3-qadam — Avtomatik ishga tushirish (eng oson yo'l)

**Linux / macOS:**

```bash
chmod +x run.sh
./run.sh
```

**Windows:**

```
run.bat
```

Bu skript avtomatik ravishda virtual muhit yaratadi, kerakli kutubxonalarni
o'rnatadi va sizdan `.env` faylini to'ldirishni so'raydi (agar hali qilmagan bo'lsangiz).

### 3-qadam (muqobil) — Qo'lda o'rnatish

Agar skriptsiz, qadam-baqadam o'zingiz qilmoqchi bo'lsangiz:

```bash
# 1) Virtual muhit yaratish (tavsiya etiladi)
python3 -m venv .venv

# 2) Virtual muhitni faollashtirish
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# 3) Kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt

# 4) .env faylini yaratish
cp .env.example .env             # Linux / macOS
copy .env.example .env           # Windows

# 5) .env faylini oching va BOT_TOKEN qiymatini
#    BotFather bergan haqiqiy token bilan almashtiring:
#    BOT_TOKEN=123456789:AAExampleTokenHereXXXXXXXXXXXXXXXXX

# 6) Botni ishga tushirish
python bot.py
```

Muvaffaqiyatli ishga tushsa, terminalda quyidagi xabarni ko'rasiz:

```
🐍 Python Funktsiyalari Boti ishga tushdi! To'xtatish uchun Ctrl+C bosing.
```

Endi Telegram'da o'zingizning botingizni toping va `/start` buyrug'ini yuboring.

Botni to'xtatish uchun terminalda **Ctrl+C** tugmalarini bosing.

## 🕹 Botdan foydalanish

| Buyruq / tugma | Vazifasi |
|---|---|
| `/start` | Botni ishga tushiradi, bosh menyuni ko'rsatadi |
| `/menu` | Bosh menyuga qaytish |
| `/help` | Yordam va qo'llanma matnini ko'rsatish |
| `/kod` | Kod yozish rejimini yoqish |
| **📖 Python Asoslari** | Darslarni ochadi (Oldingi/Keyingi tugmalar bilan) |
| **📚 Barcha Funksiyalar** | Barcha built-in funksiyalar ro'yxatini ko'rsatadi |
| **🔤 Harflar bo'yicha** | Funksiyani birinchi harfi bo'yicha qidirish |
| **🔍 Nom bo'yicha** | Funksiya nomini yozib qidirish (masalan: `len`) |
| **💡 Tasodifiy Funksiya** | Tasodifiy bir funksiyani taklif qiladi |
| **✍️ Kod Yozish va Ishga Tushirish** | Kod rejimini yoqadi — yuborgan har qanday kod ishga tushiriladi |

**Maslahat:** Kod rejimisiz ham, agar xabaringizda
`def funksiya_nomi(...):` ko'rinishidagi kod bo'lsa, bot uni avtomatik
tahlil qilib, ma'lumot beradi.

## 🔒 Xavfsizlik haqida

Kod ishga tushirish (`utils/sandbox.py`) quyidagi choralar bilan himoyalangan:

- Kod asosiy bot jarayonidan alohida **subprocess**'da ishga tushadi.
- `os`, `sys`, `subprocess`, `socket`, `shutil` kabi tizim modullarini import qilish **taqiqlangan**.
- `eval`, `exec`, `open`, `input` kabi xavfli/interaktiv funksiyalar **taqiqlangan**.
- Ishga tushirish vaqti standart holatda **5 soniya** bilan chegaralangan (`config.py`).
- Xotira ishlatilishi (Unix tizimlarida) cheklangan.
- Natija matni juda uzun bo'lsa, avtomatik qisqartiriladi.

Bu choralar botni **oddiy foydalanuvchilar uchun** xavfsiz qiladi, lekin bu
100% "bulletproof" sandbox emas — botni ommaviy/ishonchsiz auditoriyaga
ochiq serverda ishga tushirishdan oldin qo'shimcha izolyatsiya (masalan,
Docker konteyner, alohida foydalanuvchi huquqlari) qo'shishni tavsiya qilamiz.

## 🛠 Sozlamalarni o'zgartirish

`config.py` faylida quyidagi qiymatlarni o'zgartirishingiz mumkin:

```python
CODE_TIMEOUT_SECONDS = 5      # Kod ishga tushirish uchun maksimal vaqt
CODE_MAX_OUTPUT_CHARS = 3500  # Natija matnining maksimal uzunligi
CODE_MAX_MEMORY_MB = 64       # Kod uchun ajratilgan maksimal xotira
```

Yangi built-in funksiya qo'shish uchun `data/builtins_info.py` faylidagi
`BUILTINS` lug'atiga yangi yozuv qo'shing. Yangi dars qo'shish uchun
`data/lessons.py` faylidagi `LESSONS` ro'yxatiga yangi element qo'shing.

## ❓ Muammolarni bartaraf etish

- **"BOT_TOKEN topilmadi" xatosi** — `.env` faylini yaratganingizga va unda
  to'g'ri tokenni kiritganingizga ishonch hosil qiling.
- **`ModuleNotFoundError`** — `pip install -r requirements.txt` buyrug'ini
  qayta bajaring (virtual muhit faollashtirilganiga ishonch hosil qiling).
- **Bot Telegram'da javob bermayapti** — terminalda bot hali ishlab
  turganini va internet aloqasi borligini tekshiring.
- **`python3` buyrug'i topilmadi (Windows)** — o'rniga `python` buyrug'ini ishlating.

---

Loyihani xohlaganingizcha o'zgartirishingiz, kengaytirishingiz va
o'rganish uchun ishlatishingiz mumkin. Omad! 🐍✨
