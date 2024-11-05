# def calculate_factorial(n):
#     """Функция вычисляет факториал числа n."""
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)
#
# def fibonacci(n):
#     """Функция вычисляет число Фибоначчи для n."""
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# def calculate_power(base, exponent):
#     """Функция вычисляет значение степени числа base в степени exponent."""
#     return base ** exponent
#

from functools import lru_cache

@lru_cache()
def calculate_factorial(n):
    """Функция вычисляет факториал числа n."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

@lru_cache()
def fibonacci(n):
    """Функция вычисляет число Фибоначчи для n."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@lru_cache()
def calculate_power(base, exponent):
    """Функция вычисляет значение степени числа base в степени exponent."""
    return base ** exponent

print(fibonacci(6))
print(calculate_power(2, 6))
print(calculate_factorial(3))