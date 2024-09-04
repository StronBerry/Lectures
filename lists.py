# Пустой список
#empty_list = []
# Список с целыми числами
#int_list = [1, 2, 3, 4, 5]
# Список с десятичными числами
#float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
# Булевый список
#bool_list = [True, True, False]
# Список со строками
#string_list = ['Hello', 'world', '!']
# Список микс
#mix_list = [1, 1.1, True, 'Hello']

# порядковый номер элемента
#          1  2  3  4  5  6  7  8  9  10
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          0  1  2  3  4  5  6  7  8  9
# индекс элемента

#Пример:
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# выведем нулевой элемент списка
#print(clients[0])
# выведем первый элемент списка
#print(clients[1])
# выведем список целиком
#print(clients)
# выведем последний элемент списка
#print(clients[-1])
# выведем предпоследний элемент списка
#print(clients[-2])

# Изменение элементов списка
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# выведем третий элемент списка
#print(clients[3])
# изменим третий элемент списка
#clients[3] = 'Pam Halpert'
# выведем третий элемент списка
#print(clients[3])

# Срез элементов списка: list[start:stop:step]
#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# срез всего списка
# start=0 stop=10 step=1
#print(numbers[:])
# срез c нулевого по пятый элемент списка
# start=0 stop=5 step=1
#print(numbers[:5])
# срез c первого по последний элемент списка
# start=1 stop=10 step=1
#print(numbers[1:])
# срез с третьего по шестой элемент списка
# start=3 stop=6 step=1
#print(numbers[3:6])
# каждый второй элемент списка (четные индексы)
# start=1 stop=10 step=2
#print(numbers[1::2])

# Добавление элементов в конец списка
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# выведем исходный список
#print(clients)
# добавим новый элемент в список
#clients.append('Oscar Martinez')
# выведем получившийся список
#print(clients)
# считаем имя клиента с консоли
#new_client = input('Введите имя клиента: ')
# добавим этого клиента в список
#clients.append(new_client)
# выведем итоговый список
#print(clients)

# Добавление нескольких элементов в список
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# добавим несколько элементов в список
#clients.extend(['Oscar Martinez', 'Creed Bratton', 'Andy Bernard'])
# выведем получившийся список
#print(clients)
#Вывод в консоли:
#['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone', 'Oscar Martinez', 'Creed Bratton', 'Andy Bernard']

# INSERT (добавление по номеру индекса)
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# добавим элемент по индексу 1
#clients.insert(1, 'Oscar Martinez')
# выведем получившийся список
#print(clients)

# Удаление элемента с проверкой
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
#print(f'Список клиентов: {clients}')
# считываем элемент, который нужно удалить
#name = input('Введите клиента, которого нужно удалить: ')
# проверка на вхождение элемента в список
#if name in clients: # элемент есть в списке
#удаляем элемент из списка
#   clients.remove(name)
#   print('Клиент удален из списка.')
#else: # элемента в списке нет
#   print('Данного клиента в списке нет.')
#   выведем получившийся список
#print(f'Список клиентов: {clients}')

# Удаление по индексу - name.pop(номер индеска в списке)
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# удаляем клиента по индексу 0
#first_client = clients.pop(0)
#print(f'Удаленный клиент: {first_client}')
#print(f'Список клиентов: {clients}')

# Очистка списка целиком
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# удаляем все элементы из списка
#clients.clear()
#print(f'Список клиентов: {clients}')

# Получение индекса элемента
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# найдем индекс элемента Michael Scott
#index = clients.index('Michael Scott')
#print(f'Индекс элемента Michael Scott: {index}')

# Сортировка по "возрастанию" и "убыванию"
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# сортируем список в порядке возрастания
#clients.sort()
#print(f'Сортировка в порядке возрастания: {clients}')
# сортируем список в порядке убывания
#clients.sort(reverse=True)
#print(f'Сортировка в порядке убывания: {clients}')


# Посчитать количество элементов в списке
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
# выведем длину списка clients
#print(len(clients))
#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# выведем длину списка numbers
#print(len(numbers))

# Вывод на печать пронумерованный список элементов
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
#print('Клиенты нашей компании:')
# находим длину списка и вставляем её в метод range()
#for i in range(len(clients)): # i = [0, 1, 2, 3, 4]
#    print(f'{i+1}. {clients[i]}')

# IF в списке
#список клиентов, участвующих в бонусной программе
#clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']

# считываем имя клиента
#client_name = input('Введите имя клиента: ')
# проверяем, есть ли введенный клиент в списке участников
#if client_name in clients:
#    print('Клиент является участником бонусной программы')
#else:
#    print('Клиент еще не участвует в бонусной программе. Добавляем его в список участников.')
#    clients.append(client_name)

#print(f'Всего участников бонусной программы: {len(clients)}')
#print(f'Список участников: {clients}')


# Учебный пример работы со списками
#coworkers = ['Мария', 'Ангелила', 'Антонина', 'Дарья', 'Екатерина']
# вывести первый и последний элемент списка
#print(f'''Первый элемент списка: {coworkers[0]} \nПоследний элемент списка: {coworkers[-1]}''')
# вывести каждый первый элемент списка
#print(coworkers[::2])
# вывести каждый второй элемент списка
#print(coworkers[1::2])
# вывести длину списка
#print(f'Длина списка: {len(coworkers)}')
# добавить новый элемент в список
#name = input('Введите имя нового коллеги: ')
#coworkers.append(name)
# вывести длину списка
#print(f'Длина списка: {len(coworkers)}')
# проверить наличие элемента в списке
#name = input('Введите имя коллеги: ')
#if name in coworkers:
#    print('Этот коллега есть в списке')
#else:
#    print('Такого имени в списке нет')