"""
CP1404 - Practical_09
Name: Amie Neill
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test multiple UnreliableCars."""
    good_car = UnreliableCar("Toyota", 100, 90)
    average_car = UnreliableCar("Mazda", 100, 70)
    bad_car = UnreliableCar("BMW", 100, 10)

    for i in range(1, 11):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:7} drove {good_car.drive(i):3}km")
        print(f"{average_car.name:7} drove {average_car.drive(i):3}km")
        print(f"{bad_car.name:7} drove {bad_car.drive(i):3}km")

    print("Summary of Attempts:")
    print(good_car)
    print(average_car)
    print(bad_car)


main()
