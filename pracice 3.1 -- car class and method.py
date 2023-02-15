class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"

c1 = Car("Ford", "Ranger", "1992")
c2= Car("Kia", "Soul", "2014")

print(c1)
print (c2)
