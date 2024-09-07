# # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# # выводим словарь в консоль
# print(translator)




# Ключ-значение-содержимое пары. keys-values-items

# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
#
# # выводим словарь в консоль
# # ключи словаря - метод keys()
# print(f'Ключи словаря: {translator.keys()}')
# # значения словаря - метод values()
# print(f'Значения словаря: {translator.values()}')
# # пары ключ:значение - метод items()
# print(f'Пары ключ:значение словаря: {translator.items()}')




# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# # выводим английские слова, которые сохранены в словаре
# print(f'Слова в словаре: {translator.keys()}')
#
# # считываем слово, которое нужно перевести
# eng_word = input('Введите слово, которое нужно перевести: ')
# # выводим элемент словаря, полученный по ключу
# print(f'{eng_word} - {translator[eng_word]}')




# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# print(f'Исходный словарь: {translator}')
#
# # добавляем новую запись в словарь
# translator['tester'] = 'тестировщик'
# print(f'Словарь с новой записью: {translator}')
#
# # редактируем запись в словаре
# translator['tester'] = 'тестер'
# print(f'Словарь с отредактированной записью: {translator}')


# Удаление пары из словаря
# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# print(f'{translator}')
# # удаляем элемент словаря с ключом bug
# del translator['bug']
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')

# Удалить элемент словаря можно и с помощью метода pop(),
# который, как и в случае со списками, удаляет элемент и возвращает его значение в место вызова метода:
# # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# print(f'Полученный словарь: {translator}')
# # удаляем элемент словаря с ключом function и выводим его
# print(translator.pop('function'))
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')


# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# print(f'Исходный словарь: {translator}')
#
# while True:
#     # считываем слово, которое нужно удалить
#     eng_word = input('Введите слово, которое хотите удалить: ')
#
#     if eng_word in translator.keys():
#         print(f'Удаляем из словаря: {eng_word} - {translator[eng_word]}')
#         # удаляем элемент словаря с ключом eng_word
#         del translator[eng_word]
#         break
#     else:
#         print('Этого слова в словаре нет')
#
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')

# # ТО ЖЕ САМОЕ через if-then-else
# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# print(f'Исходный словарь: {translator}')
# # считываем слово, которое нужно удалить
# eng_word = input('Введите слово, которое хотите удалить: ')
# # если введенное слово есть в списке ключей словаря
# if eng_word in translator.keys():
#     print(f'Удаляем из словаря: {eng_word} - {translator[eng_word]}')
#     # удаляем элемент словаря с ключом eng_word
#     del translator[eng_word]
# else:
#     print('Этого слова в словаре нет')
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')



# # Учебное задание - телефонная книга
#
# contacts = {}
# for i in range(3):
#
#     name = input('Введите имя: ')
#     phone = input('Введите номер телефона: ')
#     contacts[name] = phone
#
# # вывести только имена из телефонной книги
# print(f'номера: {contacts.keys()}')
#
# # вывести только телефоны из телефонной книги
# print(contacts.values())
#
# print()
# for name, phone in contacts.items():
#     print(f'Контакт: {name} Телефон: {phone}')
#
# # добавить две новые записи в словарь
# print('Добавляем новые записи в словарь:')
# for i in range(2):
#     name = input('Введите имя: ')
#     phone = input('Введите номер телефона: ')
#     contacts[name] = phone
#     print('Запись добавлена в словарь')
#
# # редактируем запись в словаре:
# print('Редактируем запись в словарь:')
# print(contacts)
# name = input('Введите имя из словаря: ')
# phone = input('Введите новый номер телефона: ')
# contacts[name] = phone
# print('Запись отредактирована')
#
# # проверка на наличие записи в словаре:
# print('Проверяем наличие записи в словарь:')
# name = input('Введите имя: ')
# if name in contacts.keys():
#     del contacts[name]
#     print('Запись удалена')
# else:
#     phone = input('Введите номер телефона: ')
#     contacts[name] = phone
#     print('Запись добавлена в словарь')
#
# # выводим итоговый словарь:
# print(contacts)