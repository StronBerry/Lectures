def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

import random
import time

# Генерация списка случайных чисел
arr = [random.randint(0, 10000) for _ in range(1000)]

# Тестирование сортировки пузырьком
start_time = time.time()
sorted_arr_bubble = bubble_sort(arr.copy())
print("Bubble Sort took {:.5f} seconds".format(time.time() - start_time))
# Bubble Sort took 0.04723 seconds

# Тестирование быстрой сортировки
start_time = time.time()
sorted_arr_quick = quick_sort(arr.copy())
print("Quick Sort took {:.5f} seconds".format(time.time() - start_time))
# Quick Sort took 0.00209 seconds