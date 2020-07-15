class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    def __init__(self):
        self.scoops = []

    def add_scoops(self, scoops_to_add):
        for s in scoops_to_add:
            self.scoops.append(s)

    def display_flavors(self):
        for s in self.scoops:
            print(f"Flavor: {s.flavor}")


v = Scoop("Vanilla")
c = Scoop("Chocolate")
l = Scoop("Lemon")

b = Bowl()

b.add_scoops([v, c, l])

b.display_flavors()
