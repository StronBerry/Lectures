class User:
   login = 'user_login'
   role = 'Python Developer'


u1 = User()
u2 = User()

print(u1.login, u1.role)
print(u2.login, u2.role)

# user_login Python Developer
# user_login Python Developer

User.login = 'form_login'
User.role = 'Designer'

print(u1.login, u1.role) # form_login Designer
print(u2.login, u2.role) # form_login Designer

u1.login = 'Esbern'
u1.role = 'React developer'

print(u1.login, u1.role) # Esbern React developer
print(u2.login, u2.role) # user_login Python Developer
print(u1.__dict__, u2.__dict__) # {'login': 'Esbern', 'role': 'React developer'} {}


User.email = 'user@gmail.com'
print(User.__dict__)
print(u1.login, u1.role, u1.email)
# {'__module__': '__main__', 'login': 'user_login', 'role': 'Python Developer', '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None, 'email': 'user@gmail.com'}