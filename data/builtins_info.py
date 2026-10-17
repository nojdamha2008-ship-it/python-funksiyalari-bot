"""
Python o'rnatilgan (built-in) funksiyalari haqida ma'lumotlar bazasi.

Har bir yozuv quyidagi maydonlarga ega:
    purpose  - funksiyaning maqsadi (qisqa tavsif)
    syntax   - chaqirish sintaksisi
    params   - (nomi, tavsifi) juftliklari ro'yxati
    example  - ishlatilishiga misol (kod + natija izohi)
    category - guruh nomi (Harflar bo'yicha qidiruv va ro'yxat uchun)
"""

BUILTINS = {
    "print": {
        "purpose": "Belgilangan ma'lumotlarni konsolga chiqaradi.",
        "syntax": "print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)",
        "params": [
            ("value", "Chiqariladigan ma'lumot (cheksiz sonda bo'lishi mumkin)."),
            ("sep", "Qiymatlar orasidagi ajratuvchi (standart: bo'sh joy)."),
            ("end", "Chiqarish oxiridagi belgi (standart: yangi qator)."),
        ],
        "example": 'name = "Doston"\nprint("Salom, ", name, "!", sep="")\n# Natija: Salom, Doston!',
    },
    "len": {
        "purpose": "Obyektdagi elementlar sonini (uzunligini) qaytaradi.",
        "syntax": "len(obj)",
        "params": [("obj", "Ro'yxat, satr, kortej, lug'at yoki boshqa to'plam.")],
        "example": 'ism = "Salom"\nprint(len(ism))\n# Natija: 5',
    },
    "range": {
        "purpose": "Berilgan oraliqda ketma-ket sonlar hosil qiluvchi obyekt yaratadi.",
        "syntax": "range(start, stop, step)",
        "params": [
            ("start", "Boshlanish qiymati (ixtiyoriy, standart: 0)."),
            ("stop", "Tugash qiymati (ushbu son kiritilmaydi)."),
            ("step", "Qadam qiymati (ixtiyoriy, standart: 1)."),
        ],
        "example": "for i in range(1, 6):\n    print(i)\n# Natija: 1 2 3 4 5",
    },
    "type": {
        "purpose": "Obyektning turini (data type) qaytaradi.",
        "syntax": "type(obj)",
        "params": [("obj", "Turi aniqlanishi kerak bo'lgan istalgan obyekt.")],
        "example": 'print(type(10))\n# Natija: <class \'int\'>',
    },
    "input": {
        "purpose": "Foydalanuvchidan konsol orqali matn qabul qiladi.",
        "syntax": "input(prompt)",
        "params": [("prompt", "Ekranga chiqariladigan xabar matni (ixtiyoriy).")],
        "example": 'ism = input("Ismingiz: ")\nprint("Salom,", ism)',
    },
    "int": {
        "purpose": "Qiymatni butun son (integer) turiga o'zgartiradi.",
        "syntax": "int(x, base=10)",
        "params": [
            ("x", "O'zgartiriladigan qiymat (satr yoki son)."),
            ("base", "Agar x satr bo'lsa, sanoq sistemasi asosi."),
        ],
        "example": 'yosh = int("25")\nprint(yosh + 1)\n# Natija: 26',
    },
    "str": {
        "purpose": "Qiymatni matn (string) turiga o'zgartiradi.",
        "syntax": "str(obj)",
        "params": [("obj", "Matnga aylantiriladigan istalgan obyekt.")],
        "example": 'son = 25\nprint("Yosh: " + str(son))\n# Natija: Yosh: 25',
    },
    "float": {
        "purpose": "Qiymatni kasr son (float) turiga o'zgartiradi.",
        "syntax": "float(x)",
        "params": [("x", "O'zgartiriladigan qiymat (satr yoki son).")],
        "example": 'narx = float("19.99")\nprint(narx)\n# Natija: 19.99',
    },
    "bool": {
        "purpose": "Qiymatni mantiqiy (True/False) turga o'zgartiradi.",
        "syntax": "bool(x)",
        "params": [("x", "Tekshiriladigan qiymat.")],
        "example": "print(bool(0))\nprint(bool(5))\n# Natija: False True",
    },
    "list": {
        "purpose": "Yangi ro'yxat (list) obyekti yaratadi.",
        "syntax": "list(iterable)",
        "params": [("iterable", "Ro'yxatga aylantiriladigan to'plam (ixtiyoriy).")],
        "example": 'harflar = list("abc")\nprint(harflar)\n# Natija: [\'a\', \'b\', \'c\']',
    },
    "dict": {
        "purpose": "Yangi lug'at (dictionary) obyekti yaratadi.",
        "syntax": "dict(**kwargs)",
        "params": [("kwargs", "kalit=qiymat ko'rinishidagi argumentlar (ixtiyoriy).")],
        "example": 'odam = dict(ism="Ali", yosh=20)\nprint(odam)\n# Natija: {\'ism\': \'Ali\', \'yosh\': 20}',
    },
    "tuple": {
        "purpose": "Yangi kortej (tuple, o'zgarmas ro'yxat) obyekti yaratadi.",
        "syntax": "tuple(iterable)",
        "params": [("iterable", "Kortejga aylantiriladigan to'plam (ixtiyoriy).")],
        "example": "kord = tuple([1, 2, 3])\nprint(kord)\n# Natija: (1, 2, 3)",
    },
    "set": {
        "purpose": "Yangi to'plam (set, takrorlanmaydigan elementlar) obyekti yaratadi.",
        "syntax": "set(iterable)",
        "params": [("iterable", "To'plamga aylantiriladigan qiymatlar (ixtiyoriy).")],
        "example": "raqamlar = set([1, 2, 2, 3])\nprint(raqamlar)\n# Natija: {1, 2, 3}",
    },
    "sorted": {
        "purpose": "To'plam elementlarini saralab, yangi ro'yxat qaytaradi.",
        "syntax": "sorted(iterable, key=None, reverse=False)",
        "params": [
            ("iterable", "Saralanadigan to'plam."),
            ("key", "Saralash uchun ishlatiladigan funksiya (ixtiyoriy)."),
            ("reverse", "True bo'lsa, kamayish tartibida saralaydi."),
        ],
        "example": "sonlar = [3, 1, 2]\nprint(sorted(sonlar))\n# Natija: [1, 2, 3]",
    },
    "sum": {
        "purpose": "To'plamdagi barcha sonlarning yig'indisini hisoblaydi.",
        "syntax": "sum(iterable, start=0)",
        "params": [
            ("iterable", "Sonlardan iborat to'plam."),
            ("start", "Boshlang'ich qiymat (ixtiyoriy, standart: 0)."),
        ],
        "example": "print(sum([1, 2, 3, 4]))\n# Natija: 10",
    },
    "min": {
        "purpose": "To'plamdagi eng kichik qiymatni qaytaradi.",
        "syntax": "min(iterable)",
        "params": [("iterable", "Solishtiriladigan qiymatlar to'plami.")],
        "example": "print(min([4, 2, 9, 1]))\n# Natija: 1",
    },
    "max": {
        "purpose": "To'plamdagi eng katta qiymatni qaytaradi.",
        "syntax": "max(iterable)",
        "params": [("iterable", "Solishtiriladigan qiymatlar to'plami.")],
        "example": "print(max([4, 2, 9, 1]))\n# Natija: 9",
    },
    "abs": {
        "purpose": "Sonning mutlaq qiymatini (manfiy belgisiz) qaytaradi.",
        "syntax": "abs(x)",
        "params": [("x", "Butun yoki kasr son.")],
        "example": "print(abs(-7))\n# Natija: 7",
    },
    "round": {
        "purpose": "Sonni belgilangan aniqlikkacha yaxlitlaydi.",
        "syntax": "round(number, ndigits=None)",
        "params": [
            ("number", "Yaxlitlanadigan son."),
            ("ndigits", "Kasr qismidagi raqamlar soni (ixtiyoriy)."),
        ],
        "example": "print(round(3.14159, 2))\n# Natija: 3.14",
    },
    "pow": {
        "purpose": "Sonni darajaga oshiradi (x ni y-darajasi).",
        "syntax": "pow(x, y, z=None)",
        "params": [
            ("x", "Asos son."),
            ("y", "Daraja ko'rsatkichi."),
            ("z", "Modul (ixtiyoriy): (x**y) % z."),
        ],
        "example": "print(pow(2, 5))\n# Natija: 32",
    },
    "map": {
        "purpose": "Berilgan funksiyani to'plamning har bir elementiga qo'llaydi.",
        "syntax": "map(function, iterable)",
        "params": [
            ("function", "Har bir elementga qo'llanadigan funksiya."),
            ("iterable", "Qayta ishlanadigan to'plam."),
        ],
        "example": "sonlar = [1, 2, 3]\nnatija = list(map(lambda x: x * 2, sonlar))\nprint(natija)\n# Natija: [2, 4, 6]",
    },
    "filter": {
        "purpose": "To'plamdan shart bajarilgan elementlarni ajratib oladi.",
        "syntax": "filter(function, iterable)",
        "params": [
            ("function", "Har bir element uchun True/False qaytaruvchi funksiya."),
            ("iterable", "Filtrlanadigan to'plam."),
        ],
        "example": "sonlar = [1, 2, 3, 4, 5, 6]\njuft = list(filter(lambda x: x % 2 == 0, sonlar))\nprint(juft)\n# Natija: [2, 4, 6]",
    },
    "zip": {
        "purpose": "Bir nechta to'plamlarni juftlashtirib, birlashtiradi.",
        "syntax": "zip(*iterables)",
        "params": [("iterables", "Bir vaqtda birlashtiriladigan bir nechta to'plam.")],
        "example": 'ismlar = ["Ali", "Vali"]\nyoshlar = [20, 25]\nfor i, y in zip(ismlar, yoshlar):\n    print(i, y)',
    },
    "enumerate": {
        "purpose": "To'plam elementlarini indeks bilan birga sanab beradi.",
        "syntax": "enumerate(iterable, start=0)",
        "params": [
            ("iterable", "Sanaladigan to'plam."),
            ("start", "Indeksni boshlash qiymati (ixtiyoriy, standart: 0)."),
        ],
        "example": 'mevalar = ["olma", "uzum"]\nfor i, meva in enumerate(mevalar, start=1):\n    print(i, meva)',
    },
    "open": {
        "purpose": "Faylni ochib, u bilan ishlash uchun obyekt qaytaradi.",
        "syntax": "open(file, mode='r', encoding=None)",
        "params": [
            ("file", "Fayl nomi yoki manzili."),
            ("mode", "Rejim: 'r' o'qish, 'w' yozish, 'a' qo'shish."),
            ("encoding", "Matn kodировкаси (masalan, 'utf-8')."),
        ],
        "example": "with open('fayl.txt', 'w') as f:\n    f.write('Salom!')",
    },
    "isinstance": {
        "purpose": "Obyekt berilgan turga tegishli ekanligini tekshiradi.",
        "syntax": "isinstance(obj, classinfo)",
        "params": [
            ("obj", "Tekshiriladigan obyekt."),
            ("classinfo", "Solishtiriladigan tur (masalan, int, str)."),
        ],
        "example": "print(isinstance(5, int))\n# Natija: True",
    },
    "all": {
        "purpose": "To'plamdagi barcha elementlar True bo'lsa, True qaytaradi.",
        "syntax": "all(iterable)",
        "params": [("iterable", "Tekshiriladigan to'plam.")],
        "example": "print(all([True, True, False]))\n# Natija: False",
    },
    "any": {
        "purpose": "To'plamda kamida bitta True qiymat bo'lsa, True qaytaradi.",
        "syntax": "any(iterable)",
        "params": [("iterable", "Tekshiriladigan to'plam.")],
        "example": "print(any([False, False, True]))\n# Natija: True",
    },
    "reversed": {
        "purpose": "To'plam elementlarini teskari tartibda qaytaradi.",
        "syntax": "reversed(seq)",
        "params": [("seq", "Teskari aylantiriladigan ketma-ketlik.")],
        "example": "print(list(reversed([1, 2, 3])))\n# Natija: [3, 2, 1]",
    },
    "format": {
        "purpose": "Qiymatni belgilangan formatga moslab, matn ko'rinishida qaytaradi.",
        "syntax": "format(value, format_spec='')",
        "params": [
            ("value", "Formatlanadigan qiymat."),
            ("format_spec", "Format qoidasi (masalan, '.2f')."),
        ],
        "example": 'print(format(3.14159, ".2f"))\n# Natija: 3.14',
    },
    "divmod": {
        "purpose": "Bo'linma va qoldiqni birgalikda kortej ko'rinishida qaytaradi.",
        "syntax": "divmod(a, b)",
        "params": [("a", "Bo'linuvchi son."), ("b", "Bo'luvchi son.")],
        "example": "print(divmod(17, 5))\n# Natija: (3, 2)",
    },
    "id": {
        "purpose": "Obyektning xotiradagi noyob identifikatorini qaytaradi.",
        "syntax": "id(obj)",
        "params": [("obj", "Istalgan Python obyekti.")],
        "example": "x = 10\nprint(id(x))  # xotiradagi manzil (natija har xil bo'lishi mumkin)",
    },
    "help": {
        "purpose": "Obyekt yoki modul haqida qo'llanma (dokumentatsiya) chiqaradi.",
        "syntax": "help(obj)",
        "params": [("obj", "Ma'lumot olinadigan obyekt yoki modul nomi.")],
        "example": "help(str)\n# Satr (str) turi haqida to'liq ma'lumot chiqadi",
    },
    "dir": {
        "purpose": "Obyektning barcha metod va atributlari ro'yxatini qaytaradi.",
        "syntax": "dir(obj)",
        "params": [("obj", "Ro'yxati chiqariladigan obyekt (ixtiyoriy).")],
        "example": "print(dir(str))\n# Natija: ['capitalize', 'casefold', ... ]",
    },
    "iter": {
        "purpose": "Obyektdan iterator (aylanish obyekti) yaratadi.",
        "syntax": "iter(obj)",
        "params": [("obj", "Iteratsiya qilinadigan to'plam.")],
        "example": "it = iter([1, 2, 3])\nprint(next(it))\n# Natija: 1",
    },
    "next": {
        "purpose": "Iteratordan navbatdagi elementni oladi.",
        "syntax": "next(iterator, default)",
        "params": [
            ("iterator", "iter() orqali yaratilgan obyekt."),
            ("default", "Element tugaganda qaytariladigan qiymat (ixtiyoriy)."),
        ],
        "example": "it = iter([1, 2])\nprint(next(it))\nprint(next(it))\n# Natija: 1  2",
    },
}

# Alifbo bo'yicha qidiruv uchun mavjud harflarni aniqlash
AVAILABLE_LETTERS = sorted({name[0].upper() for name in BUILTINS})


def find_by_name(name: str):
    """Nomi bo'yicha funksiya ma'lumotini topadi (parentez va bo'sh joysiz)."""
    clean = name.strip().lower().replace("()", "").split("(")[0]
    return BUILTINS.get(clean)


def names_starting_with(letter: str):
    letter = letter.upper()
    return sorted(n for n in BUILTINS if n.upper().startswith(letter))
