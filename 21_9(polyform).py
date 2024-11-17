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

    def display_info(self):
        print("Savings account №{}, balance: {} {}, interest rate: {}".format(
            self.account_number, self.balance,
            self.currency, self.interest_rate))

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

    def display_info(self):
        print("Checking account №{}, balance: {}{}, transaction fee: {}".format(
            self.account_number, self.balance,
            self.currency, self.transaction_fee))


# Создаем экземпляры классов
savings_account1 = SavingsAccount("SAV-001", 0.05, 'EUR')
savings_account2 = SavingsAccount("SAV-002", 0.07)
savings_account3 = SavingsAccount("SAV-003", 0.1, 'RUB')
checking_account1 = CheckingAccount("CHK-001", 2.50)

# Поменяем их в контейнер -- список
accounts = [savings_account1, savings_account2, savings_account3, checking_account1]
for account in accounts:
    account.display_info()

# Savings account №SAV-001, balance: 0 EUR, interest rate: 0.05
# Savings account №SAV-002, balance: 0 USD, interest rate: 0.07
# Savings account №SAV-003, balance: 0 RUB, interest rate: 0.1
# Checking account №CHK-001, balance: 0USD, transaction fee: 2.5