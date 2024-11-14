# class User:
#    login = 'user_login'
#    role = 'Python Developer'
#
#    # объявление метода
#    def demo_method_print():
#        print('Method call')
#
# # вызов метода
# User.demo_method_print()
#
# # Method call
class User:
    login = 'user_login'
    role = 'Python Developer'
    def demo_method_print(self):
       print(f'Method call by {self}')

u1 = User()
u2 = User()
print(u1)

u1.demo_method_print()
User.demo_method_print(u1)
User.demo_method_print(u2)

# <__main__.User object at 0x7fcce544a3e0>
# Method call by <__main__.User object at 0x7fcce544a3e0>
