# OOP Exercise 4: Class Inheritance
#
# Given:
#
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def bus_capacity(self, capacity=50):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")


class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 200, 10)
print(school_bus.bus_capacity())

