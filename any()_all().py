# #Функция any() возвращает True, если хотя бы один элемент итерируемого объекта истинен
# # (или, другими словами, имеет значение True). В противном случае возвращает False:
#
# values = [False, False, True, False]
# result = any(values)
# print(result)
# # True
#
# #Функция all() возвращает True, если все элементы итерируемого объекта истинны.
# # Если хотя бы один элемент ложен, возвращает False:
#
# values = [False, False, True, True]
# result = all(values)
# print(result)
# # False

# data = [3, 1, 9, 7]
# assert all(x > 0 for x in data), "Not all elements are positive"
# # Ошибки нет, все числа положительные
# assert any(x == 5 for x in data), "The value 5 is not in the list"
# # AssertionError: The value 5 is not in the list
#
# errors = ["", "", "Page not found", ""]
# assert not any(errors), "There were errors during testing!"
# # AssertionError: There were errors during testing!


# test_results = [True, True, True, True]
# assert all(test_results), "Not all tests passed!"
# # Все тесты действительно прошли проверку, ошибка не поднята

# Без any
data = [0, 1, 2, 3]
contains_positive = False
for num in data:
   if num > 0:
       contains_positive = True
       break
# C any
data = [0, 1, 2, 3]
contains_positive = any(num > 0 for num in data)