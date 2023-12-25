class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
    def deposit(self, x):
        self.balance += x
        self.transactions.append(f'На баланс зачисленно: {x}руб')
    def withdraw(self, y):
        self.balance -= y
        self.transactions.append(f'С баланаса списано: {y}руб')
    def add_interest(self):
        percent = self.balance + self.balance * self.interest_rate
        self.transactions.append(f'Проценты по вкладу: {self.balance * self.interest_rate} руб')
    def history(self):
        print('\n'.join(self.transactions))

user = BankAccount(100000, 0.05)
user.deposit(15000)
user.withdraw(7500)
user.add_interest()
user.history()
print(f'Баланс: {user.balance}руб')
