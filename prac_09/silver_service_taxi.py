"""
CP1404 - Practical_09
Name: Amie Neill
Silver Service Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a SilverServiceTaxi."""
    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness
