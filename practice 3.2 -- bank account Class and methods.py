class BankAccount:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def withdraw(self, amount):
        if self.account_balance < amount:
            print('Insufficient balance.')
        else:
            self.account_balance -= amount
            print(f'Withdrawn {amount}. New balance is {self.account_balance}.')

    def deposit(self, amount):
        self.account_balance += amount
        print(f'Deposited {amount}. New balance is {self.account_balance}.')
