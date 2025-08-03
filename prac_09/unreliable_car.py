"""
CP1404 - Practical_09
Name: Amie Neill
Unreliable Car
"""
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an unreliable car."""
    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability
