class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    def __init__(self):
        self.scoops = []

    def add_scoops(self, scoops_to_add):
        if len(self.scoops) == 3:
            print("Max amount of scoops (3) added!")
            return

        for s in scoops_to_add:
            self.scoops.append(s)

            if len(self.scoops) == 3:
                break

    def display_flavors(self):
        for s in self.scoops:
            print(f"Flavor: {s.flavor}")


v = Scoop("Vanilla")
c = Scoop("Chocolate")
l = Scoop("Lemon")
p = Scoop("Pistachio")
cd = Scoop("Cookie Dough")

b = Bowl()

b.add_scoops([v, c, l, p, cd])

b.display_flavors()
