class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


class VerbosePerson(Person):
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


p = Person("Malik")
vp = VerbosePerson("Makayla", 22)

p.greet()
vp.greet()
