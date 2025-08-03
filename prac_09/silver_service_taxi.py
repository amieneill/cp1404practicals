"""
CP1404 - Practical_09
Name: Amie Neill
Silver Service Taxi
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a SilverServiceTaxi."""
    flagfall = 4.5
    
    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
    
    def get_fare(self):
        """Get the fare price."""
        return self.flagfall + super().get_fare()