# class User:
#     PASSWORD_MIN_LEN = 5
#     PASSWORD_MAX_LEN = 16
#
#     def __init__(self, login, password, name, email, role):
#         self.__validate_password(password)
#         self.__login = login
#         self.__password = password
#         self.name = name
#         self.email = email
#         self.role = role
#
#     @classmethod
#     def __validate_password(cls, password):
#         if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN and type(password) == str):
#             raise AttributeError('Password not valid')
#
#     def get_login(self):
#         return self.__login
#
#     def set_login(self, new_login):
#         self.__login = new_login
#
#     def get_password(self):
#         return self.__password
#
#     def set_password(self, new_password):
#         self.__validate_password(new_password)
#         self.__password = new_password
#
#     login = property(get_login, set_login)
#     password = property(get_password, set_password)
#
#
# u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')
# print(u1.__dict__)
# u1.password = 'Krop88'
# print(u1.password)

# {'_User__login': 'JohnD', '_User__password': 'majesk123',
# 'name': 'John Doe', 'email': 'john.doe@example.com', 'role': 'TechLead'}
# Krop88

# u1.password = '124'
# # AttributeError: Password not valid


# Синтаксис создания и обращения к @PROPERTY

# class DemoClass:
#    def __init__(self):
#        self.__some_private_property = None
#
#    @property
#    def some_private_property(self):
#        """Геттер для свойства __some_private_property."""
#        return self.__some_private_property
#
#    @some_private_property.setter
#    def some_private_property(self, value):
#        """Сеттер для свойства __some_private_property."""
#        self.__some_private_property  = value
#
# demo_object = DemoClass()
# # Используем @some_private_property.setter
# demo_object.some_private_property = 15
# # Используем @property
# print(demo_object.some_private_property)


class User:
    PASSWORD_MIN_LEN = 5
    PASSWORD_MAX_LEN = 16

    def __init__(self, login, password, name, email, role):
        self.__validate_password(password)
        self.__login = login
        self.__password = password
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def __validate_password(cls, password):
        if not (cls.PASSWORD_MIN_LEN <= len(password) <= cls.PASSWORD_MAX_LEN):
            raise AttributeError('Password not valid')

    # Оборачиваем геттер атрибута __login декоратором @property
    # Превращаем метод в свойство, которое можно получать
    @property
    def login(self):
        return self.__login

    # Оборачиваем геттер атрибута __password декоратором @property
    # Превращаем метод в свойство, которое можно получать
    @property
    def password(self):
        return self.__password

    # Оборачиваем сеттер атрибута __login декоратором @login.setter
    # Добавляем возможность изменять свойство login, созданное ранее
    @login.setter
    def login(self, login):
        self.__login = login

    # Оборачиваем сеттер атрибута __password декоратором @password.setter
    # Добавляем возможность изменять свойство password, созданное ранее
    @password.setter
    def password(self, password):
        self.__validate_password(password)
        self.__password = password

u1 = User("JohnD", "majesk123", "John Doe", "john.doe@example.com", 'TechLead')

# Используются методы с декоратором @property
print(u1.login, u1.password)
# Используется метод с декоратором  @login.setter
u1.login = 'JohnDaveric'
# Используется метод с декоратором  @password.setter
u1.password = 'AdfgjdfS'

print(u1.login, u1.password)
# JohnD majesk123