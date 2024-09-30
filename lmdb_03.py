# # Фильтруем четные числа из списка
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]


# Список словарей
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Сортируем по возрасту
sorted_people = sorted(people, key=lambda person: person['age'])

print(sorted_people)
# Вывод: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
