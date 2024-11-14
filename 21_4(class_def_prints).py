class User:
   login = 'user_login'
   role = 'Python Developer'

   def demo_method_print(self):
       print(f'Method call by {self}')

   def show_attrs(self):
       print(f'Login: {self.login}, role: {self.role}')
#
# u1 = User()
# u1.show_attrs()
#
# # Login: user_login, role: Python Developer

u1 = User()
u1.login  = 'Gridin'
u1.role = 'TechLead'
u1.show_attrs()

# Login: Gridin, role: TechLead