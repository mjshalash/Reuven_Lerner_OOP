class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

v = Scoop("Vanilla")
c = Scoop("Chocolate")
l = Scoop("Lemon")

for s in [v, c, l]:
    print(s.flavor)