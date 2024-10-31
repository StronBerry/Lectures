def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    return deposit, withdraw

deposit, withdraw = make_account(100)
print(deposit(15))
# 115
print(withdraw(1))
# 85
print(deposit(15))

# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
#
# print(times3(times5(2)))



# def make_printer(msg):
#     message = "Hello1 " + msg
#     def printer():
#         print(message)
#     return printer
#
# printer = make_printer("World1")
# printer()