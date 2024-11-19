def bubble_sort(array):
    n = len(array)
    # Проходим по массиву несколько раз
    for i in range(n):
        # Флаг для отслеживания перестановок
        swapped = False
        # Сравниваем и меняем местами соседние элементы
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # Если перестановок не было, массив отсортирован
        if not swapped:
            break
    return array

import random

not_sorted = [random.randint(1, 50) for _ in range(10)]
print(not_sorted)


after_bubble = bubble_sort(not_sorted)
print(after_bubble)
