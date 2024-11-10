class User:
   login = 'user_login'
   role = 'Python Developer'

u1 = User()
print(type(u1)) # <class '__main__.User'>

print(type(u1) == User) # True
print(isinstance(u1, User)) # True