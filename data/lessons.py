"""
Python asoslari bo'yicha darslar ro'yxati.

Har bir dars: id, emoji, title, content (HTML formatda), example (kod misoli).
Darslar tartib raqami bo'yicha navigatsiya qilinadi (Oldingi/Keyingi tugmalar).
"""

LESSONS = [
    {
        "id": "l01",
        "emoji": "🐍",
        "title": "Python nima?",
        "content": (
            "Python — bu sodda va tushunarli sintaksisga ega, yuqori darajali "
            "dasturlash tili. U veb-saytlar, sun'iy intellekt, ma'lumotlar tahlili, "
            "avtomatlashtirish va hattoki Telegram botlar (masalan, shu bot!) "
            "yaratish uchun ishlatiladi.\n\n"
            "Kod .py kengaytmali faylda yoziladi va <code>python fayl.py</code> "
            "buyrug'i orqali ishga tushiriladi."
        ),
        "example": 'print("Salom, Python!")',
    },
    {
        "id": "l02",
        "emoji": "📦",
        "title": "O'zgaruvchilar",
        "content": (
            "O'zgaruvchi — bu ma'lumotni xotirada saqlash uchun nom. Python'da "
            "o'zgaruvchi e'lon qilishda tur ko'rsatish shart emas — Python buni "
            "avtomatik aniqlaydi.\n\n"
            "Qoidalar: nom harf yoki pastki chiziq (_) bilan boshlanadi, raqam "
            "bilan boshlanmaydi, katta-kichik harf farqlanadi."
        ),
        "example": 'ism = "Amir"\nyosh = 20\nboyi = 1.75\nprint(ism, yosh, boyi)',
    },
    {
        "id": "l03",
        "emoji": "🔢",
        "title": "Ma'lumot turlari",
        "content": (
            "Asosiy ma'lumot turlari:\n"
            "• <b>int</b> — butun son (masalan: 10, -5)\n"
            "• <b>float</b> — kasr son (masalan: 3.14)\n"
            "• <b>str</b> — matn (masalan: \"Salom\")\n"
            "• <b>bool</b> — mantiqiy qiymat (True yoki False)\n"
            "• <b>list</b>, <b>tuple</b>, <b>dict</b>, <b>set</b> — to'plamlar\n\n"
            "Turi aniqlash uchun <code>type()</code> funksiyasidan foydalaniladi."
        ),
        "example": 'print(type(10))     # <class \'int\'>\nprint(type(3.14))   # <class \'float\'>\nprint(type("hi"))   # <class \'str\'>',
    },
    {
        "id": "l04",
        "emoji": "➕",
        "title": "Operatorlar",
        "content": (
            "• <b>Arifmetik:</b> + - * / // % **\n"
            "• <b>Solishtirish:</b> == != > < >= <=\n"
            "• <b>Mantiqiy:</b> and, or, not\n"
            "• <b>Tayinlash:</b> = += -= *= /=\n\n"
            "<code>//</code> — butun qismli bo'lish, <code>%</code> — qoldiq, "
            "<code>**</code> — darajaga oshirish."
        ),
        "example": "print(7 // 2)   # 3\nprint(7 % 2)    # 1\nprint(2 ** 3)   # 8\nprint(5 > 3 and 2 < 4)  # True",
    },
    {
        "id": "l05",
        "emoji": "🔀",
        "title": "Shartli operatorlar (if)",
        "content": (
            "<code>if</code>, <code>elif</code>, <code>else</code> yordamida "
            "shartga qarab turli kod bloklari bajariladi. Python'da bloklar "
            "figurali qavs emas, <b>indentatsiya (bo'sh joy)</b> bilan ajratiladi."
        ),
        "example": (
            "yosh = 18\n"
            "if yosh >= 18:\n"
            "    print(\"Kattasiz\")\n"
            "elif yosh >= 13:\n"
            "    print(\"O'smirsiz\")\n"
            "else:\n"
            "    print(\"Bolasiz\")"
        ),
    },
    {
        "id": "l06",
        "emoji": "🔁",
        "title": "Sikllar (for, while)",
        "content": (
            "<b>for</b> — to'plam elementlari bo'yicha aylanish uchun.\n"
            "<b>while</b> — shart to'g'ri bo'lguncha takrorlash uchun.\n\n"
            "<code>break</code> — siklni to'xtatadi, <code>continue</code> — "
            "joriy qadamni o'tkazib yuboradi."
        ),
        "example": (
            "for i in range(3):\n"
            "    print(\"for:\", i)\n\n"
            "n = 0\n"
            "while n < 3:\n"
            "    print(\"while:\", n)\n"
            "    n += 1"
        ),
    },
    {
        "id": "l07",
        "emoji": "📋",
        "title": "Ro'yxatlar (list)",
        "content": (
            "Ro'yxat — bir nechta qiymatlarni tartib bilan saqlaydigan, "
            "<b>o'zgaruvchan (mutable)</b> to'plam. Kvadrat qavs "
            "<code>[]</code> bilan yoziladi.\n\n"
            "Foydali metodlar: <code>append()</code>, <code>remove()</code>, "
            "<code>sort()</code>, <code>pop()</code>, <code>insert()</code>."
        ),
        "example": (
            "mevalar = [\"olma\", \"uzum\"]\n"
            "mevalar.append(\"nok\")\n"
            "print(mevalar)        # ['olma', 'uzum', 'nok']\n"
            "print(mevalar[0])     # olma"
        ),
    },
    {
        "id": "l08",
        "emoji": "🔒",
        "title": "Kortejlar (tuple)",
        "content": (
            "Kortej — ro'yxatga o'xshaydi, lekin yaratilgandan so'ng "
            "<b>o'zgartirib bo'lmaydi (immutable)</b>. Doiraviy qavs "
            "<code>()</code> bilan yoziladi. O'zgarmas ma'lumotlar uchun qulay."
        ),
        "example": (
            "kordinata = (41.3, 69.2)\n"
            "print(kordinata[0])   # 41.3\n"
            "# kordinata[0] = 5   # Xato! Kortejni o'zgartirib bo'lmaydi"
        ),
    },
    {
        "id": "l09",
        "emoji": "🗂",
        "title": "Lug'atlar (dict)",
        "content": (
            "Lug'at — <b>kalit:qiymat</b> juftliklarini saqlaydi. Jingalak "
            "qavs <code>{}</code> bilan yoziladi. Ma'lumotni kalit orqali "
            "tez topish mumkin."
        ),
        "example": (
            "odam = {\"ism\": \"Ali\", \"yosh\": 25}\n"
            "print(odam[\"ism\"])     # Ali\n"
            "odam[\"shahar\"] = \"Toshkent\"\n"
            "print(odam)"
        ),
    },
    {
        "id": "l10",
        "emoji": "🎯",
        "title": "To'plamlar (set)",
        "content": (
            "To'plam — <b>takrorlanmaydigan</b> va tartibsiz elementlar "
            "guruhi. Jingalak qavs bilan yoziladi, lekin lug'atdan farqli "
            "faqat qiymatlarni saqlaydi. Takrorlarni olib tashlash uchun qulay."
        ),
        "example": (
            "raqamlar = {1, 2, 2, 3, 3, 3}\n"
            "print(raqamlar)   # {1, 2, 3}\n"
            "raqamlar.add(4)\n"
            "print(raqamlar)   # {1, 2, 3, 4}"
        ),
    },
    {
        "id": "l11",
        "emoji": "🔤",
        "title": "Satrlar (string)",
        "content": (
            "Satr — matn ma'lumoti, qo'shtirnoq yoki bitta tirnoq bilan "
            "yoziladi. Foydali metodlar: <code>.upper()</code>, "
            "<code>.lower()</code>, <code>.split()</code>, <code>.strip()</code>, "
            "<code>.replace()</code>. f-string orqali qiymatlarni matn ichiga "
            "qo'yish mumkin."
        ),
        "example": (
            "ism = \"Dilnoza\"\n"
            "print(f\"Salom, {ism}!\")\n"
            "print(ism.upper())     # DILNOZA\n"
            "print(len(ism))        # 7"
        ),
    },
    {
        "id": "l12",
        "emoji": "🧩",
        "title": "Funksiyalar (def)",
        "content": (
            "Funksiya — qayta-qayta ishlatsa bo'ladigan kod bo'lagi. "
            "<code>def</code> kaliti bilan e'lon qilinadi, <code>return</code> "
            "orqali natija qaytaradi. Argumentlarga standart qiymat berish "
            "mumkin."
        ),
        "example": (
            "def salomlash(ism, salom=\"Salom\"):\n"
            "    return f\"{salom}, {ism}!\"\n\n"
            "print(salomlash(\"Aziz\"))\n"
            "print(salomlash(\"Nodira\", \"Xayrli tong\"))"
        ),
    },
    {
        "id": "l13",
        "emoji": "⚡",
        "title": "Lambda funksiyalar",
        "content": (
            "Lambda — nomi bo'lmagan, bitta qatorli qisqa funksiya. Odatda "
            "<code>map()</code>, <code>filter()</code>, <code>sorted()</code> "
            "kabi funksiyalar bilan birga ishlatiladi."
        ),
        "example": (
            "kvadrat = lambda x: x ** 2\n"
            "print(kvadrat(5))   # 25\n\n"
            "sonlar = [3, 1, 2]\n"
            "print(sorted(sonlar, key=lambda x: -x))  # [3, 2, 1]"
        ),
    },
    {
        "id": "l14",
        "emoji": "📥",
        "title": "Modullar",
        "content": (
            "Modul — funksiyalar va o'zgaruvchilarni saqlaydigan .py fayl. "
            "<code>import</code> orqali boshqa modulni loyihaga qo'shish "
            "mumkin. Python o'zida ko'plab tayyor modullarga ega "
            "(math, random, datetime va h.k.)."
        ),
        "example": (
            "import math\nimport random\n\n"
            "print(math.sqrt(16))       # 4.0\n"
            "print(random.randint(1, 6))  # 1 dan 6 gacha tasodifiy son"
        ),
    },
    {
        "id": "l15",
        "emoji": "📁",
        "title": "Fayllar bilan ishlash",
        "content": (
            "<code>open()</code> funksiyasi fayl bilan ishlash imkonini "
            "beradi. <code>with</code> operatoridan foydalanish tavsiya "
            "etiladi — u faylni avtomatik yopadi."
        ),
        "example": (
            "with open(\"fayl.txt\", \"w\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"Salom, fayl!\")\n\n"
            "with open(\"fayl.txt\", \"r\", encoding=\"utf-8\") as f:\n"
            "    print(f.read())"
        ),
    },
    {
        "id": "l16",
        "emoji": "🚨",
        "title": "Xatoliklarni qayta ishlash",
        "content": (
            "<code>try</code>/<code>except</code> orqali dastur ishlashi "
            "davomida yuzaga keladigan xatoliklarni ushlab, dastur to'xtab "
            "qolishining oldini olish mumkin. <code>finally</code> har doim "
            "bajariladigan blok."
        ),
        "example": (
            "try:\n"
            "    son = int(\"abc\")\n"
            "except ValueError:\n"
            "    print(\"Bu son emas!\")\n"
            "finally:\n"
            "    print(\"Tekshiruv tugadi\")"
        ),
    },
    {
        "id": "l17",
        "emoji": "🏗",
        "title": "OOP asoslari (class)",
        "content": (
            "Ob'ektga yo'naltirilgan dasturlash (OOP) — kod va ma'lumotni "
            "<b>class</b> ichida birlashtirish. <code>__init__</code> — "
            "obyekt yaratilganda avtomatik chaqiriladigan metod (konstruktor)."
        ),
        "example": (
            "class Odam:\n"
            "    def __init__(self, ism):\n"
            "        self.ism = ism\n\n"
            "    def salomlash(self):\n"
            "        return f\"Salom, men {self.ism}\"\n\n"
            "odam = Odam(\"Kamola\")\n"
            "print(odam.salomlash())"
        ),
    },
    {
        "id": "l18",
        "emoji": "✨",
        "title": "List comprehension",
        "content": (
            "Ro'yxatni qisqa va chiroyli yaratish usuli — bitta qatorda "
            "sikl va shartni birlashtiradi."
        ),
        "example": (
            "kvadratlar = [x**2 for x in range(1, 6)]\n"
            "print(kvadratlar)   # [1, 4, 9, 16, 25]\n\n"
            "juftlar = [x for x in range(10) if x % 2 == 0]\n"
            "print(juftlar)      # [0, 2, 4, 6, 8]"
        ),
    },
    {
        "id": "l19",
        "emoji": "🧰",
        "title": "Foydali built-in funksiyalar",
        "content": (
            "Python juda ko'p tayyor (built-in) funksiyalarga ega: "
            "<code>len()</code>, <code>sum()</code>, <code>sorted()</code>, "
            "<code>range()</code>, <code>type()</code> va boshqalar.\n\n"
            "💡 Ularning har biri haqida to'liq ma'lumot olish uchun bosh "
            "menyudagi <b>\"🔍 Nom bo'yicha Qidiruv\"</b> tugmasidan "
            "foydalaning — funksiyaning nomini yozing (masalan: "
            "<code>print</code> yoki <code>len</code>)."
        ),
        "example": 'print(sum([1, 2, 3]), sorted([3, 1, 2]), len("Python"))',
    },
]


def get_lesson(index: int):
    if 0 <= index < len(LESSONS):
        return LESSONS[index]
    return None


TOTAL_LESSONS = len(LESSONS)
