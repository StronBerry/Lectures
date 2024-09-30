# from functools import reduce
#
# # Список чисел
# numbers = [1, 2, 3, 4, 5]
#
# # Вычисляем произведение всех чисел
# product = reduce(lambda x, y: x * y, numbers)
#
# print(product)  # Вывод: 120


def make_incrementor(n):
    return lambda x: x + n

# Создаем функции, которые добавляют 5 и 10
increment_by_5 = make_incrementor(5)
increment_by_10 = make_incrementor(10)

# Используем их
print(increment_by_5(3))  # Вывод: 8
print(increment_by_10(3))  # Вывод: 13


# # Lambda с тернарным оператором
# max_num = lambda a, b: a if a > b else b
# 
# print(max_num(10, 20))  # Вывод: 20
