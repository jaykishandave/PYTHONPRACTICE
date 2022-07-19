# OOP Exercise 6: Class Inheritance


class Vehicle:
    Color_name = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100


class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 200, 10,50)
print(
    f"Color:{school_bus.Color_name} and Vehicle name:{school_bus.name} and Speed: {school_bus.max_speed} Bus Capacity: {school_bus.bus_capacity()} Bus Mileage: {school_bus.mileage}")
