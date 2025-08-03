"""
CP1404 - Practical_09
Name: Amie Neill
Unreliable Car
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an unreliable car."""
    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive an unreliable car."""
        random_number = randint(1, 100)
        if random_number > self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance
