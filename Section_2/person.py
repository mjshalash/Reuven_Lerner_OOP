class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


p1 = Person("Malik", "malik@email.com", "555-555-5555")
p2 = Person("Mak", "mak@email.com", "666-666-6666")
p3 = Person("Josh", "josh@email.com", "777-777-7777")

print("Before.....")
for p in [p1, p2, p3]:
    print("-------------------")
    print(f"Name:  {p.name}")
    print(f"Email: {p.email}")
    print(f"Phone: {p.phone}")
    print("-------------------")

p2.email = "mak@daddy.com"

print()
print()
print("After.....")
for p in [p1, p2, p3]:
    print("-------------------")
    print(f"Name:  {p.name}")
    print(f"Email: {p.email}")
    print(f"Phone: {p.phone}")
    print("-------------------")

