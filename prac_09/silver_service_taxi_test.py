"""
CP1404 - Practical_09
Name: Amie Neill
Silver Service Taxi Test
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Audi", 100, 2)
    taxi.drive(20)
    print(taxi)
    print(f"Fare price: ${taxi.get_fare()}")


main()
