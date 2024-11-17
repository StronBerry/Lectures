class User:
   PASSWORD_MIN_LEN = 5
   PASSWORD_MAX_LEN = 16

   def __init__(self, login, password, name, email, role):
       # Добавили проверку пароля в инициализатор
       self.__validate_password(password)
       self.__login = login
       self.__password = password

   def get_login_password(self):
       return self.__login, self.__password

   @classmethod
   def __validate_password(cls, password):
      if not(cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == str):
          raise AttributeError('Password not valid')

   def set_login_password(self, login, password):
       self.__validate_password(password)
       self.__login = login
       self.__password = password

u1 = User("JohnD", "qwe21", "John Doe", "john.doe@example.com", 'TechLead')
print(u1.get_login_password())

# AttributeError: Password not valid

print(dir(u1))
print(u1._User__login, u1._User__password)