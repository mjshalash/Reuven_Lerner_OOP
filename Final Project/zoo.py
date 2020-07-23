class Wolf(object):
    def __init__(self, color):
        self.color = color
        self.legs = 4
        self.species = "Wolf"

    def __repr__(self):
        output = f"{self.color} {self.species}, {self.legs} legs \n"
        return output


class Sheep(object):
    def __init__(self, color):
        self.color = color
        self.legs = 4
        self.species = "Sheep"

    def __repr__(self):
        output = f"{self.color} {self.species}, {self.legs} legs \n"
        return output


class Snake(object):
    def __init__(self, color):
        self.color = color
        self.legs = 0
        self.species = "Snake"

    def __repr__(self):
        output = f"{self.color} {self.species}, {self.legs} legs \n"
        return output


class Parrot(object):
    def __init__(self, color):
        self.color = color
        self.legs = 2
        self.species = "Parrot"

    def __repr__(self):
        output = f"{self.color} {self.species}, {self.legs} legs \n"
        return output


class Cage(object):
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *args):
        for a in args:
            self.animals.append(a)

    def __repr__(self):
        output = f" Cage {self.cage_id} \n"
        counter = 1
        for a in self.animals:
            output += f"{counter} {a} \n"
            counter += 1

        return output

class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for c in args:
            self.cages.append(c)

    def __repr__(self):
        output = f""
        for c in self.cages:
            output += f"{c} \n"

        return output

    def animals_by_color(self, color):
        output = f""
        counter = 1
        for c in self.cages:
            for a in c.animals:
                if a.color == color:
                    output += f"{counter} {a} \n"
                    counter += 1

        return output

    def number_of_legs(self):
        total_legs = 0
        for c in self.cages:
            for a in c.animals:
                total_legs += a.legs

        return total_legs


wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)    #  black wolf, 4 legs
print(sheep1)    #  white sheep, 4 legs
print(sheep2)    #  white sheep, 4 legs
print(snake)    #   brown snake, 0 legs
print(parrot)    #  black parrot, 2 legs

c1 = Cage(1)   # ID numbers
c1.add_animals(wolf, sheep1, sheep2)
print(c1)

#    Cage 1:
# 1 black wolf, 4 legs
# 2 white sheep, 4 legs
# 3 white sheep, 4 legs

c2 = Cage(2)
c2.add_animals(snake, parrot)
print(c2)

#    Cage 2:
# 1 brown snake, 0 legs
# 2 black parrot, 2 legs

z = Zoo()
z.add_cages(c1, c2)
print(z)

#     Cage 1:
# 1 black wolf, 4 legs
# 2 white sheep, 4 legs
# 3 white sheep, 4 legs
#     Cage 2:
# 1 brown snake, 0 legs
# 2 black parrot, 2 legs

print(z.animals_by_color('black'))
# 1 black wolf, 4 legs
# 2 black parrot, 2 legs

print(z.number_of_legs())
#     14