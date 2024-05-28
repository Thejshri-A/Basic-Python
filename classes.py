# Classes
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_my_model(self):
        print(f"I'm a {self.make} {self.model}")


# Objects
my_car = Vehicle("Tesla", "Model S")
print("My Car", my_car)
print("My Car Make", my_car.make)
print("My Car Model", my_car.model)
my_car.moves()
my_car.get_my_model()

# Inheritance


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies Along ... ")


class Truck(Vehicle):
    def moves(self):
        print("Rolls Along ... ")


class Golfcart(Vehicle):
    pass


cessna = Airplane("Cessna", "Skyhawk", "FA-22345")
tata = Truck("TATA", "Mini")
golfwagon = Golfcart("Gigi", "G150")

cessna.get_my_model()
cessna.moves()
tata.get_my_model()
tata.moves()
golfwagon.get_my_model()
golfwagon.moves()

# Polymorphism

for i in (my_car, cessna, tata, golfwagon):
    print("::::")
    i.get_my_model()
    i.moves()
