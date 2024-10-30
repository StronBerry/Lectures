x = 20

def change_global_var():
	global x
	x = 30

print(x)  # Вывод: 20
change_global_var()
print(x)  # Вывод: 30

# БЕЗ объявления X
# def change_global_var():
# 	global x
#
# 	x = 30
#
#
# change_global_var()
# print(x)
# # 30