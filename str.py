#Импортировать "десятиричный калькулятор
#from decimal import Decimal
#print(Decimal("90") == 90)

#Преобразование классов чисел
#a = 64
#b = float(a)
#print(b)
#print(type(b))
#print (a)

#Преобразование классов чисел
#from decimal import Decimal
#a = Decimal("4.8")
#b = float(a)
#print(b)
#print(type(b))

#математическое округление
#a = round(12.5)
#print(a)
#print(type(a))

#Округление чисел "вниз"
#import math
#print(math.floor(50.99))

#Округление чисел "вверх"
#import math
#print(math.ceil(50.00001))

#Вычисление модуля
#print(abs(88))
#print(abs(-88))

#варианты округлений секунд до года "вниз"
#import math
#seconds_since_birthdate = 1145455353
#a = seconds_since_birthdate
#print(int(seconds_since_birthdate / 365 / 24 / 60 / 60))
# ИЛИ
#print(math.floor(seconds_since_birthdate / 365 / 24 / 3600))
# ИЛИ
#print(a // (365 * 24 * 60 * 60))

#Варианты записи и сравнения строчных данных (str)
#a = "string"
#b = 'string'
#c = """string"""
#d = '''string'''
#print(a is b is c is d)
#print(a == b == c == d)

#Срезы строк данных из строки
#a = "проприетарный"[3]
#в ответе будет
#a = "п"
#a = 'сколопендра'[1:4]
#в ответе будет
#a = 'кол'

#Вариант "до" [23:] и "после" [:23]
#Пример
#text = "2023-02-15 14:21:46.353 ERROR message: Ай, случилася беда!"
#print(text[39:])


#Обратная индексация (срез с конца)
#Варианты для консоли:
#    >>> "просто строка"[-2]
#    'к'
#    >>> "просто строка"[-6:]
#    'строка'
#    >>> "просто строка"[:-6]
#    'просто '
#    >>> "И это просто строка"[-14:-6]
#    ' просто '
#    >>> "А это не просто строка"[6:-7]
#    'не просто'
#Каждый второй символ в строке:
#>>> "1234567890"[::2]
# '13579'
#   >>> "1234567890"[1:-1:2]
#   '2468'
#В обратном порядке:
#>>> 'абвгдеёжзиклмнопрст'[::-1]
#'тсрпонмлкизжёедгвба'

#Учебный пример:
#string = "ываываппавосстань, сын трёхголового дракона!"
#if len(string) < 42:
#    print("length error: длина строки составляет", len(string), "символов")
#else:
#    print(string[7:42:3])

#Индексы
#text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
#template = 'message: '
#index = text.index(template)
#print(text[index + len(template):])

#Подсчет слов в string:
#string = "Давным-давно, в далёкой-далёкой галактике жил-был слесарь."
#print(len(string.split()))

#Find
#text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
#template = 'message: '
#index = text.find(template)
#if index != -1:
#    print(text[index + len(template):])

#In
#text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
#template = 'message: '
#if template in text:
#index = text.index(template)
#print(text[index + len(template):])

#Count
#print("abracadabra".count("a"))

#Начинается с ...
# name = "internal_attr_2"
#if not name.startswith("_"):
#    print(name)

#Заканчивается ...
#word = "мыш"
#if word.endswith("ь"):
#    print("Это существительное женского рода:", word)
#if not word.endswith("ь"):
#    print("нифига не женского рода:", word)

#Метод islower() проверяет, все ли символы строки являются строчными:
#"abcde".islower()
#Метод isupper() проверяет, все ли символы строки являются прописными:
#"ABC".isupper()
#Метод istitle() проверяет, начинается ли строка с заглавной буквы и следуют ли за ней строчные:
#"Незнайка".istitle()
#Метод isnumeric() проверяет, состоит ли представленная строка только из цифр:
#"12345".isnumeric()
#Метод isalpha() проверяет, наоборот, не содержит ли строка чего-либо помимо букв алфавита (любого):
#"абвгдсCDEF".isalpha()

#Проверка, что все буквы - латинские
# string = "dd"
#if len(string) == 0:
#    print(False)
#else:
#    print(string.isascii())

#Проверка, что string заканчивается на "_"
#string = "aaa_"
#print(string.endswith("_"))

#Пример подсчета слов в строке
#string = "Я типа пошёл типа вчера гулять типа вот типа ага."
#print(string.count("типа"))

#разделение строк на слова по пробелу
#a = "А роза упала на лапу Азора"
#print(a.split())
#... по символу ''
#a = "А роза упала на лапу Азора"
#print(a.split('п'))

#Метод strip() по сути — «скинуть лишнее»
#a = "\t \n   \t text \n\f\t  "
#print(a.strip())

#Убрать конкретные символы
#a = "авбвааббв Три слона на перепутье бббаааввв"
#print(a.strip("абв"))

#Удалить конкретную последовательность в начале строки
#.removeprefix()

#Удалить из конца строки
#.removesuffix()

#Преобразовать все символы в строчные/заглавные
#.lower() / .upper()
#.casefold() превращает все СиМвоЛы в сравниваемые

#Замена символов в строках
#replace("что", "на что")

#Подсчет сочетаний в строке
#string = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!"
#substring = "тр"
#print(string.casefold().count(substring.casefold()))

#Удаление символов с конца строки
#string = "(Что бы это ни значило :)"
#print(string.rstrip("!().?"))

#.FORMAT()
#Подставление значений в string с номерами (начало с "0")
#a = "A {1} has {0} legs and a {2} has {0} legs. So what's the difference between a {1} and a {2}?"
#print(a.format(4, "cat", "dog"))

#Подставление значений в string с заданными значениями)
#a = "A {animal1} has {number} legs and a {animal2} has {number} legs. So what's the difference between a {animal1} and a {animal2}?"
#print(a.format(animal1="cat", animal2="dog", number=4))

#отображение количества точек после запятой в float
#fl = 3.1223467
#print("{:.3f}".format(fl))

#Зачем-то добавление отступов
#name, author = "Незнайка", "Николай Носов"
#print("{: <30} | {: >30}".format(name, author))

#F - форматирование через подставление значений в {}
#year = 1992
#month = "сентября"
#day = 12
#print(f"Это произошло {day} {month} {year} года.")

#Можно работать с числами в таких подставлениях через F
#car_cost = 120000
#manager, count = "Петров", 12
#print("Продажи автомобилей в прошлом месяце:")
#print(f"Менеджер {manager} продал {count} автомобилей, что принесло {car_cost * count} единиц валюты.")

#Превращение string в int
#a = "50"
#b = int(a)
#print(type(b))

#spade_cards = "🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮"
#print(spade_cards)

#4 варианта подставлений чисел/текста в текст
#count = 4
#name = "Саутуарк"
#a = "Сегодня утром %d автомобиля и %d омнибуса проехали по мосту %s." % (count, count, name)
#b = "Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.".format(count=count, name=name)
#c = f"Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}."

