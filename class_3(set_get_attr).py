class User:
   login = 'user_login'
   role = 'Python Developer'


u1 = User()
print(getattr(User, 'email', False)) # False

# Установка (либо изменение) нового атрибута класса
setattr(User, 'email', 'user@gmail.com')

# Установка (либо изменение) локального атрибута экземпляру класса
setattr(u1, 'login', 'DEIvanov')

print(u1.login, u1.role, u1.email) #DEIvanov Python Developer user@gmail.com

# Получение скрытых атрибутов
# class User:
#    login = 'user_login'
#    role = 'Python Developer'
#
#
# some_hidden_attr_name = 'email'
# print(getattr(User, some_hidden_attr_name, False))
#
# # False



