class ShoppingCart(object):
    def __init__(self, contents):
        self.contents = contents

    def __len__(self):
        num_items = 0
        for item in self.contents:
            num_items += 1

        return num_items

    def __repr__(self):
        ret_str = f""

        for item in self.contents:
            target = self.contents[item]
            target_quant = self.contents[item]["Quantity"]
            target_ppu = self.contents[item]["PPU"]
            ret_str += f"{target}  {target_quant} {target_ppu} ${target_quant*target_ppu} \n"

        ret_str += f"----------------------------------"
        ret_str += f"                               {self.total()}"
        return ret_str

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




sc = ShoppingCart({})
sc.add('book', 30, 1)
sc.add('toothbrush', 3, 4)
sc.remove('book', 5)
print(len(sc))
print(sc)
# sc.display()
# print(sc.total())


