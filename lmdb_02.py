# # Создаем lambda-функцию для сложения двух чисел
# sum_numbers = lambda a, b: a + b
#
# # Пример использования lambda-функции
# result = sum_numbers(3, 5)
#
# print(result)  # Вывод: 8

# Пример использования lambda с map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]
