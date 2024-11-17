# внесение дублированных элементов в базовый класс

# Объявляем базовый класс
class Account:
    # Добавили атрибут уровня класса
    withdrawal_limit = 1000

    # Добавили инициализатор в базовый класс
    def __init__(self, account_number, currency='USD'):
        self.account_number = account_number
        self.balance = 0
        self.currency = currency

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
        # Вызываем инициализатор класса-родителя
        Account.__init__(self, account_number, currency)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # Расчёт и начисление процентов на остаток по счёту
        interest = self.balance * self.interest_rate
        self.balance += interest

# Объявляем еще один дочерний класс, наследуемый от базового
class CheckingAccount(Account):
    def __init__(self, account_number, transaction_fee, currency='USD'):
        # Вызываем инициализатор класса-родителя
        Account.__init__(self, account_number, currency)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        # Вычет комиссии за транзакцию
        self.balance -= self.transaction_fee

checking_account = CheckingAccount(account_number="CHK-001",
                                   transaction_fee=2.50,
                                   currency='USD')

print("Checking account №{}, balance: {}, transaction fee: {}".format(
    checking_account.account_number,
    checking_account.balance,
    checking_account.transaction_fee
))

# Checking account №CHK-001, balance: 0, transaction fee: 2.5