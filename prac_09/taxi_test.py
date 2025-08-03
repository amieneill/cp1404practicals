"""
CP1404 - Practical_09
Name: Amie Neill
Taxi Test
"""
from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, Current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Current fare: ${my_taxi.get_fare():.2f}")


main()
