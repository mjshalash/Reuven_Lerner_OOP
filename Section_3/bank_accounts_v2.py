import numpy as np

class Account(object):
    def __init__(self, tran_history):
        self.tran_history = tran_history

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []

    def add_account(self, acc_to_add):
        self.accounts.append(acc_to_add)

    def all_balances(self):
        balances = []
        for a in self.accounts:
            balances.append(sum(a.tran_history))

        return balances

    def total_balance(self):
        total = 0

        for a in self.accounts:
            total += sum(a.tran_history)

        return total


p1 = Person("Malik", "malik@email.com", "555-555-5555")

# Account Transactions
acc_1 = [1000.00, -10.30, 5.00]
acc_2 = [1000.00, -10.00, 10.00]

a1 = Account(acc_1)
a2 = Account(acc_2)

p1.add_account(a1)
p1.add_account(a2)

print(p1.all_balances())
print(p1.total_balance())