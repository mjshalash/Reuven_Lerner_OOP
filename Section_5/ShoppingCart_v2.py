class ShoppingCart(object):
    def __init__(self, contents):
        self.contents = contents

    def add(self, i_name, i_price, i_quant):
        self.contents[i_name] = {"PPU": i_price, "Quantity": i_quant}

    def remove(self, i_name, quant_rem):

        if self.contents[i_name]["Quantity"] - quant_rem <= 0:
            self.contents.pop(i_name)
        else:
            self.contents[i_name]["Quantity"] -= quant_rem

    def display(self):
        print(self.contents)

    def total(self):
        cart_total = 0
        for item in self.contents:
            cart_total = cart_total + (self.contents[item]["PPU"] * self.contents[item]["Quantity"])

        return cart_total


class OnlineShoppingCart(ShoppingCart):
    def __init__(self, contents):
         super().__init__(contents)

    def total(self):
        cart_total = 0
        for item in self.contents:
            print(item)
            cart_total = cart_total + (self.contents[item]["PPU"]*self.contents[item]["Quantity"])

        return 10+cart_total+(cart_total*0.05)


sc = ShoppingCart({})
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)
sc.remove('book', 5)
sc.display()
print(sc.total())

sc = OnlineShoppingCart({})
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)
sc.remove('book', 5)
sc.display()
print(sc.total())


