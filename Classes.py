# A Class is an user-defined blueprint or template used to create objects. it allows you to group data (attributes) and functions (methods) together into a single, logical unit

class Vehicle:
    def __init__(self, Make, Model):
        self.Make = Make
        self.Model = Model
    def moves(self):
        print("It can move.")

    def honks(self):
        print("Honks")

    def get_make_model(self):
        print(f"I'm a {self.Make} {self.Model}.")

my_car = Vehicle('Tesla','Roadster')

my_car.get_make_model()

my_car.moves()

my_car.honks()


your_car = Vehicle('Toyota', 'Innova_crysta')
your_car.get_make_model()
your_car.honks()
your_car.moves()


# Inheritance is a mechanism that allows a class to inherit properties and methods from another class. It is a way to reuse code and create a hierarchy of classes. 

#super() is a built-in function used to gain access to the methods and attributes of a parent (or sibling) class. It returns a temporary proxy object that delegates method calls to a superclass, allowing you to extend and reuse existing functionality without rewriting code. 

class Airplane(Vehicle):
    def __init__(self,Make, Model, faa_id):
        super().__init__(Make,Model)
        self.faa_id = faa_id
        print("Flies along...")
        print(f"My faa id is {self.faa_id}.")

class Truck(Vehicle):
    def moves(self):
        print("Trundles along....")


my_plane = Airplane("Boeing", "747", "N981AV")
my_plane.get_make_model()
my_plane.moves()
my_plane.honks()

my_truck = Truck("Tata", "Truck")
my_truck.get_make_model()
my_truck.moves()
my_truck.honks()

class Golfcart(Vehicle):
    def moves(self):
        print("Moves along....")

Golfwagen = Golfcart("Volkswagen","Golfcart")
Golfwagen.get_make_model()
Golfwagen.moves()
Golfwagen.honks()   

# Polymorphism is a core OOP concept that allows a single interface or method to be used for different types of objects or implementations such as methods, operators, or a class to behave differently based on the context in which it is used. 

print('\n\n')

for v in (my_car, your_car, my_plane, my_truck, Golfwagen):
    v.get_make_model()
    v.moves()
    v.honks()

print('\n\n')
 

