class Bank(object):
    def __init__(self, starting_assets):
        self.assets = starting_assets


class Loan(object):
    def __init__(self, amount, bank):
        if bank.assets > amount:
            self.amount = amount
        else:
            raise ValueError('Bank has insufficient assets to grant loan')

    def repay(self, bank, amount):
        bank.assets += amount


b = Bank(700)
l1 = Loan(500, b)
l2 = Loan(200, b)
#l3 = Loan(700, b)  # raises an exception -- ValueError to indicate no money
l1.repay(b, 700)
l3 = Loan(700, b)  # now it'll work, because the bank has sufficient funds
