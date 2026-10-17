"""Botning statik matnlari (xush kelibsiz, yordam va h.k.)."""

WELCOME_TEXT = (
    "👋 Salom, {first_name}!\n"
    "<b>Python Funktsiyalari va Asoslari Boti</b>ga xush kelibsiz! 🐍\n\n"
    "Bu yerda siz:\n"
    "📖 Python asoslarini bosqichma-bosqich o'rganasiz\n"
    "🔍 Har qanday built-in funksiya haqida to'liq ma'lumot olasiz\n"
    "🧩 O'zingiz yozgan <code>def</code> funksiyangiz haqida tahlil olasiz\n"
    "✍️ Kodingizni to'g'ridan-to'g'ri shu yerda yozib, ishga tushirib ko'rasiz\n\n"
    "Boshlash uchun quyidagi tugmalardan birini tanlang 👇"
)

HELP_TEXT = (
    "⚙️ <b>Yordam &amp; Qo'llanma</b>\n\n"
    "<b>Asosiy tugmalar:</b>\n"
    "📖 <b>Python Asoslari</b> — o'zgaruvchilardan OOP'gacha 19 ta qisqa darslar.\n"
    "📚 <b>Barcha Funksiyalar</b> — barcha built-in funksiyalar ro'yxati.\n"
    "🔤 <b>Harflar bo'yicha</b> — funksiyani birinchi harfi bo'yicha qidirish.\n"
    "🔍 <b>Nom bo'yicha</b> — funksiya nomini yozib qidirish (masalan: <code>len</code>).\n"
    "💡 <b>Tasodifiy funksiya</b> — o'rganish uchun tasodifiy funksiya taklif qiladi.\n"
    "✍️ <b>Kod yozish va ishga tushirish</b> — bu rejimda yuborgan har qanday "
    "Python kodingiz xavfsiz muhitda ishga tushiriladi va natija sizga qaytariladi.\n\n"
    "<b>Qo'shimcha imkoniyat:</b>\n"
    "Kod rejimisiz ham, agar xabaringizda <code>def funksiya_nomi(...):</code> "
    "ko'rinishidagi funksiya bo'lsa — bot uni avtomatik tahlil qilib, "
    "parametrlari va vazifasi haqida ma'lumot beradi.\n\n"
    "<b>Buyruqlar:</b>\n"
    "/start — botni qayta ishga tushirish\n"
    "/menu — bosh menyuni ko'rsatish\n"
    "/kod — kod yozish rejimini yoqish\n"
    "/help — shu yordam matnini ko'rsatish\n\n"
    "⚠️ Xavfsizlik uchun <code>os</code>, <code>sys</code>, <code>subprocess</code> "
    "kabi tizim modullaridan foydalanish taqiqlangan, ishga tushirish vaqti "
    "esa bir necha soniya bilan chegaralangan."
)

CODE_MODE_ON_TEXT = (
    "✍️ <b>Kod yozish rejimi yoqildi!</b>\n\n"
    "Endi menga istalgan Python kodini yuboring — men uni xavfsiz muhitda "
    "ishga tushirib, natijasini sizga qaytaraman.\n\n"
    "Masalan, quyidagini yuborib ko'ring:\n"
    "<code>for i in range(3):\n    print(\"Salom\", i)</code>\n\n"
    "Chiqishga <b>\"🔚 Kod rejimidan chiqish\"</b> tugmasini bosing."
)

CODE_MODE_OFF_TEXT = "🔚 Kod yozish rejimidan chiqdingiz. Bosh menyuga qaytdingiz."

SEARCH_PROMPT_TEXT = (
    "🔍 <b>Nom bo'yicha qidiruv</b>\n\n"
    "Qidirmoqchi bo'lgan funksiya nomini yozing (masalan: <code>print</code>, "
    "<code>len</code> yoki <code>sorted</code>)."
)

NOT_FOUND_TEXT = (
    "❌ \"{query}\" nomli funksiya ma'lumotlar bazasidan topilmadi.\n\n"
    "📚 \"Barcha Funksiyalar Ro'yxati\" tugmasi orqali mavjud funksiyalarni ko'rishingiz mumkin."
)

FALLBACK_TEXT = (
    "🤔 Kechirasiz, xabaringizni tushunmadim.\n\n"
    "Agar Python funksiyasi haqida bilmoqchi bo'lsangiz — uning nomini yozing "
    "(masalan: <code>print</code>).\n"
    "Agar o'z kodingizni sinab ko'rmoqchi bo'lsangiz — \"✍️ Kod Yozish va "
    "Ishga Tushirish\" tugmasini bosing.\n\n"
    "Yoki quyidagi menyudan foydalaning 👇"
)
