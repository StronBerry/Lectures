#numbers_tuple = (1, 2, 3, 4, 5, 6)
#numbers_list = [1, 2, 3, 4, 5, 6]
# определим размер с помощью .__sizeof__()
#print(f'''Размер кортежа: {numbers_tuple.__sizeof__()}''')
#print(f'''Размер кортежа: {numbers_list.__sizeof__()}''')

#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# выведем нулевой элемент кортежа
#print(numbers[0])
# выведем третий элемент кортежа
#print(numbers[3])
# выведем последний элемент кортежа
#print(numbers[-1])

# Срез по кортежу
#numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# срез всего кортежа
# start=0 stop=10 step=1
#print(numbers[:])
# срез c нулевого по пятый элемент кортежа
# start=0 stop=5 step=1
#print(numbers[:5])
# срез c первого по последний элемент кортежа
# start=1 stop=10 step=1
#print(numbers[1:])
# срез с третьего по шестой элемент кортежа
# start=3 stop=6 step=1
#print(numbers[3:6])
# каждый второй элемент кортежа (четные индексы)
# start=1 stop=10 step=2
#print(numbers[1::2])

#numbers = (0, 1, 2, 3, 4, 5)
    # переберем элементы кортежа
#    for elem in numbers:
#        print(elem)

# Проверка нахождения элемента в кортеже
#numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#    num = int(input('Введите число: '))
#    if num in numbers:
#        print('Это число есть в кортеже.')
#    else:
#        print('Этого числа нет в кортеже.')

# Замерить длину кортежа
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        # найдем длину кортежа
#        len(numbers)

# Присвоить имена данным в кортеже
#user = ('Michael', 'Scott', 40)
# разложим кортеж на отдельные переменные
#name, surname, age = user
#print(name)
#print(surname)
#print(age)

# МНОЖЕСТВА!

# создаем множество из списка с помощью set()
#numbers = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9])
#print(numbers)

# создаем множество с помощью {}
#numbers = {1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9}
#print(numbers)

# перебор элементов множества
#numbers = {1, 1, 2, 2, 3, 4, 5}
        # перебор элементов множества
#        for elem in numbers:
#            print(elem)

# Проверка на нахождение элемента в множестве + длина
#numbers = {1, 1, 2, 2, 3, 4, 5}
#        num = int(input('Введите число: '))
#        if num in numbers:
#            print('Это число есть во множестве.')
#        else:
#            print('Этого числа нет во множестве.')
    # найдем длину множества
#    len(numbers)

#добавить элемент в множество - set.add(elem).
#        numbers = {1, 1, 2, 2, 3, 4, 5}
#        # добавим элемент в множество
#        numbers.add(6)
#        print(numbers)

#удалить элемент из множества - set.remove(elem).
#        numbers = {1, 1, 2, 2, 3, 4, 5}
#        # удалим элемент из множества
#        numbers.remove(1)
#        print(numbers)

#очистить множество - set.clear().
#    numbers = {1, 1, 2, 2, 3, 4, 5}
#    # удалим все элементы из множества
#    numbers.clear()
#    print(numbers)

# Учебные примеры

# 1 Кортеж:
#family = ('Я', 'кот', 'Сестра Соня', 'Мама', 'Папа')
# вывести первый и последний элемент кортежа
#print(f'''Первый элемент: {family[0]}
#            Последний элемент: {family[-1]}''')
# вывести каждый второй элемент кортежа
#print(family[1::2])

# 2 Множество:

#numbers = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#num = int(input('Введите число: '))
#if num in numbers:
#    print('Удаляем число из множества')
#    numbers.remove(num)
#else:
#    print('Добавляем число в множество')
#    numbers.add(num)
#print(f'Длина множества: {len(numbers)}')
#print(numbers)

