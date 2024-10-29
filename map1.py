# map(function, iterable, ...)
#
# squared = map(lambda x: x**2, [1, 2, 3, 4])
#
# print(list(squared))
# # [1, 4, 9, 16]

# numbers_int = map(int, ['1', '2', '3', '4'])
# print(list(numbers_int))
# # [1, 2, 3, 4]

# numbers_int = map(int, ['1', '2', '3', '4'])
#
#
# print(type(numbers_int))
# # <class 'map'>
# print(numbers_int)
# # <map object at 0x000002178F525970>

# numbers_int = map(int, ['1', '2', '3', '4'])
#
#
# for n in numbers_int:
#    print(n, type(n))
# # 1 <class 'int'>
# # 2 <class 'int'>
# # 3 <class 'int'>
# # 4 <class 'int'>
#


# Список тестовых случаев
test_cases = [1, 0, 5, 6, -1, -3, -1, 2, -2]


# Функция тестирования, которая возвращает True, если число положительное, и False, если отрицательное.
def test_case(n):
   return n > 0


# Применяем функцию ко всем тестовым случаям
results = map(test_case, test_cases)


# Преобразовываем итератор в список
results_list = list(results)


print(results_list)
# [True, False, False, True, False]