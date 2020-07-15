import numpy as np

class Account(object):
    def __init__(self, tran_history):
        self.tran_history = tran_history


# Account Transactions
acc_1 = [1000.00, -10.30, 5.00]
acc_2 = [1000.00, -10.00, 10.00]

a1 = Account(acc_1)
a2 = Account(acc_2)


for acc in [a1, a2]:
    print(f"Number of Transactions: {len(acc.tran_history)}")
    print(f"Average Amount per Transaction: {np.average(acc.tran_history)}")
    print(f"Current Balance: {sum(acc.tran_history)}")