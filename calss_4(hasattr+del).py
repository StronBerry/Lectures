# class User:
#    login = 'user_login'
#    role = 'Python Developer'
#
#
# User.email = 'email_template@gmail.com'
# print(hasattr(User, 'email')) # True
#
# del User.email
# print(hasattr(User, 'email')) # False

# ИЛИ

class User:
   login = 'user_login'
   role = 'Python Developer'


User.email = 'email_template@gmail.com'
print(hasattr(User, 'email')) # True

delattr(User, 'email')
print(hasattr(User, 'email')) # False

# Различие между hasattr() и getattr() с опциональным третьим параметром в том,
# что hasattr() возвращает либо True, либо False, а getattr() либо значение атрибута,
# если он существует, либо значение третьего параметра, переданного ей, если не существует.




