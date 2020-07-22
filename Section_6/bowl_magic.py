class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"


class Bowl(object):
    def __init__(self, scoops):
        self.scoops = scoops

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

    def __len__(self):
        total = 0
        for s in self.scoops:
            total += 1

        return total

    def __repr__(self):
        str_ret = f""
        idx = 1

        for s in self.scoops:
            str_ret += f"{idx}) {s} \n"
            idx += 1

        return str_ret


class BigBowl(Bowl):
    def __init__(self, scoops):
        super().__init__(scoops)

    def add_scoops(self, scoops_to_add):
        if len(self.scoops) == 5:
            print("Max amount of scoops (5) added!")
            return

        for s in scoops_to_add:
            self.scoops.append(s)

            if len(self.scoops) == 5:
                break


v = Scoop("Vanilla")
c = Scoop("Chocolate")
l = Scoop("Lemon")
p = Scoop("Pistachio")
cd = Scoop("Cookie Dough")
print(v)

b = Bowl([])
b.add_scoops([v, c, l, p, cd])
b.display_flavors()
print(len(b))
print(b)
print()
print()
# bb = BigBowl([])
# bb.add_scoops([v, c, l, p, cd])
# bb.display_flavors()
# print(len(bb))
