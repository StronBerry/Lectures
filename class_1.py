# Объявляем класс User
class User:
   def __init__(self, name, email, create_at, is_email_verified):
       self.name = name
       self.email = email
       self.create_at = create_at
       self.is_email_verified = is_email_verified

# Создаем двух пользователей
u1 = User('Peter', 'peterrobertson@mail.com', '2019-05-05', True)
u2 = User('Julia Donaldson', 'juliadonaldson@mail.com', '2019-06-13', True)

# Выводим имя и почту пользователя u1
print(u1.name, u1.email)

# Выводим имя и почту пользователя u2
print(u2.name, u2.email)
# Peter peterrobertson@mail.com
# Julia Donaldson juliadonaldson@mail.com