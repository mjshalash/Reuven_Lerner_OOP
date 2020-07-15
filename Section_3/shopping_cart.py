class ShoppingCart(object):
    def __init__(self):
        self.contents = {}

    def add(self, i_name, i_price, i_quant):
        self.contents[i_name] = {"PPU": i_price, "Quantity": i_quant}

    def remove(self, i_name, quant_rem):

        if self.contents[i_name]["Quantity"] - quant_rem <= 0:
            self.contents.pop(i_name)
        else:
            self.contents[i_name]["Quantity"] -= quant_rem

    def display(self):
        print(self.contents)


sc = ShoppingCart()

sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)

sc.remove('book', 5)

sc.display()