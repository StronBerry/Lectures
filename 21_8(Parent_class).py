# Объявляем базовый класс
class Account:
    # Добавили атрибут уровня класса
    withdrawal_limit = 1000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        # Добавили ограничение на снятие
        if amount > self.withdrawal_limit:
            print("Withdrawal limit exceeded")
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Объявляем дочерний класс, наследуемый от базового
class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate, currency='USD'):
        # Инициализация объекта сберегательного счёта
        self.account_number = account_number
        self.balance = 0
        self.interest_rate = interest_rate
        self.currency = currency

    def calculate_interest(self):
        # Расчёт и начисление процентов на остаток по счёту
        interest = self.balance * self.interest_rate
        self.balance += interest

# Объявляем еще один дочерний класс, наследуемый от базового
class CheckingAccount(Account):
    def __init__(self, account_number, transaction_fee, currency='USD'):
        # Инициализация объекта текущего счёта
        self.account_number = account_number
        self.balance = 0
        self.transaction_fee = transaction_fee
        self.currency = currency

    def deduct_transaction_fee(self):
        # Вычет комиссии за транзакцию
        self.balance -= self.transaction_fee

# Создание экземпляров класса
savings_account = SavingsAccount(account_number="SAV-001",
                                 interest_rate=0.05,
                                 currency='USD')

# Использование методов класса
savings_account.deposit(1000)               # Внесение депозита на счёт
savings_account.calculate_interest()        # Расчёт и начисление процентов

# Выводим информацию о сберегательном счёте
print("Savings account №{}, balance: {}, interest rate: {}".format(
    savings_account.account_number,
    savings_account.balance,
    savings_account.interest_rate
))

# Savings account №SAV-001, balance: 1050.0, interest rate: 0.05

# checking_account = CheckingAccount(account_number="CHK-001",
#                                    transaction_fee=2.50,
#                                    currency='USD')
#
# # Использование методов класса
# checking_account.deposit(1000)              # Внесение депозита на счёт
# checking_account.withdraw(500)              # Снятие суммы со счёта
# checking_account.deduct_transaction_fee()   # Снятие комиcсии
#
# print("Checking account №{}, balance: {}, transaction fee: {}".format(
#     checking_account.account_number,
#     checking_account.balance,
#     checking_account.transaction_fee
# ))

# Checking account №CHK-001, balance: 497.5, transaction fee: 2.5

# Создание экземпляра класса
checking_account = CheckingAccount(account_number="CHK-001",
                                   transaction_fee=2.50,
                                   currency='USD')
print('Withdrawal limit: {}'.format(checking_account.withdrawal_limit))