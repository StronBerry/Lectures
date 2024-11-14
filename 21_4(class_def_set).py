class User:
   login = 'user_login'
   role = 'Python Developer'

   def set_login(self, login):
       self.login = login

   def set_role(self, role):
       self.role = role

   def show_attrs(self):
       print(f'Login: {self.login}, role: {self.role}')


u1 = User()
u1.set_login('Gridin')
u1.set_role('TechLead')
u1.show_attrs()

# Login: Gridin, role: TechLead

print(u1.__dict__)
u2 = User()
print(u2.__dict__)

# {'login': 'Gridin', 'role': 'TechLead'}
# {}