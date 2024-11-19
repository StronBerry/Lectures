def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


import random

not_sorted = [random.randint(1, 50) for _ in range(10)]
print(not_sorted)


after_quick = quick_sort(not_sorted)
print(after_quick)
