# some_variable1 = 10
# some_variable2 = 'Variable2'
#
#
# def some_func(list1, list2):
# 	concatenated_list = list1 + list2
# 	return concatenated_list

# def magic_func():
# 	print(some_variable1)
# 	print('У меня есть доступ к переменной some_variable1!')
#
# some_variable1 = 10
# some_variable2 = 'Variable2'
#
# magic_func()
# # 10
# # У меня есть доступ к переменной some_variable1!

some_variable1 = 10
some_variable2 = 'Variable2'

# Очевидно, в этой части программы с нашими переменными всё будет в порядке:
print(some_variable1, some_variable2)
# Вывод на экран: 10 Variable2

def some_func(list1, list2):
	# Объявляем переменные с именами из глобального пространства имен в локальном:
	some_variable1 = 1
	some_variable2 = 'LocalVariable2'

	# Посмотрим, что выведет программа:
	print(some_variable1, some_variable2)

	concatenated_list = list1 + list2
	return concatenated_list

# Здесь функция должна будет вывести переменные some_variable1 и some_variable2 из локального пространства имен:
result = some_func([1, 2], [3, 4])
# Вывод на экран: 1 LocalVariable2

# Проверяем, изменились ли ссылки переменных some_variable1 и some_variable2:
print(some_variable1, some_variable2)
# Вывод на экран: 10 Variable2

