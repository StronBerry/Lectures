def my_function(arg1, arg2, arg3="default", arg4=None):
   print(arg1, arg2, arg3, arg4)


# Позиционные аргументы
my_function(1, 2, 3)

# Ключевые аргументы
my_function(arg1=1, arg4=4, arg2=2, arg3=3)

# Обязательные и необязательные аргументы
my_function(1, 2, arg4=4)