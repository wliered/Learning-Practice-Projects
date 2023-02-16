class Person:
    def __init__(self, name, age, address):
        self.name= name
        self.age=age
        self.address=address

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nAddress: {self.address}"

p1 = Person("Sarah", 35, "603 Main Street")

print(p1)