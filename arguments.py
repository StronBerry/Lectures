# def show_card(name, age, sex): # <- это параметры
#    print("Name: {}\nAge: {}\nSex: {}".format(name, age, sex))
#
# show_card('Lev', 22, 'Male')  # <- это аргументы
#    # Name: Lev
#    # Age: 22
#    # Sex: Male

# def show_card(name, age, sex):
#    print("Name: {}\nAge: {}\nSex: {}".format(name, age, sex))
#
# show_card(age=222, sex='Male', name='Lev') # Используем ключи

# def power(base, exponent=2):  # "exponent" - параметр со значением по умолчанию
#    return base ** exponent
#
# print(power(10))  # "10" - позиционный аргумент, "exponent" будет равен 2 = 100
# print(power(10, 3))
# # 100
# print(power(10, exponent=4))
# # 10000

# def send_request(url, method="GET", headers=None, body=None):
#    print(f"Отправка {method}-запроса на {url}")
#
#    if headers:
#        print(f"Заголовки: {headers}")
#
#    if body:
#        print(f"Тело запроса: {body}")
#
#    # Здесь мог бы быть код для отправки HTTP-запроса,
#    # но для простоты мы просто печатаем детали запроса.
#    return
#
# # Использование функции
# send_request("http://example.com")
# # Отправка GET-запроса на http://example.com
#
# send_request("http://example.com", "POST", body={"key": "value"})
# # Отправка POST-запроса на http://example.com
# # Тело запроса: {'key': 'value'}
#
# send_request("http://example.com", headers={"Authorization": "Bearer token"})
# # Отправка GET-запроса на http://example.com
# # Заголовки: {'Authorization': 'Bearer token'}


# def create_start_list(start_value, lst=None):
#    if lst is None:
#        lst=[]
#    lst.append(start_value)
#    return lst
#
# l1 = create_start_list(1)
# print(l1)
# # [1]
# l2 = create_start_list(2)
# print(l2)
# # [2]

