# Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття та поповнення коштів на
# рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
        else:
            print('Сумма должна быть положительной')

    def withdraw(self, amount):
        if amount < 0:
            print('Сумма должна быть положительной')
        elif amount < self.balance:
            self.balance = self.balance - amount
        else:
            print('На вашем счету недостаточно средств.')

    def __str__(self):
        return f'На вашем счету {self.balance}$'


my_account = BankAccount(1000)
my_account.withdraw(100)
my_account.deposit(300)
print(my_account)
