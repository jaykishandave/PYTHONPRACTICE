# OOP Exercise 5: Define a property that must have the same value for every class instance (object)

class Vehicle:
    Color_name = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def bus_capacity(self, capacity=50):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")


class Bus(Vehicle):
    pass    


school_bus = Bus("Volvo", 200, 10)
print(f"Color:{school_bus.Color_name} and Vehicle name:{school_bus.name} and Speed: {school_bus.max_speed} Bus Capacity: {school_bus.bus_capacity()} Bus Mileage: {school_bus.mileage}")
