"""
CP1404 - Practical_09
Name: Amie Neill
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test multiple UnreliableCars."""
    car_one = UnreliableCar("Good Car", 100, 90)
    car_two = UnreliableCar("Okay Car", 100, 70)
    car_three = UnreliableCar("Bad Car", 100, 10)

    for i in range(1, 11):
        print(f"Attempt to drive {i}km:")
        print(f"{car_one.name} drove {car_one.drive(i)}km")
        print(f"{car_two.name} drove {car_two.drive(i)}km")
        print(f"{car_three.name} drove {car_three.drive(i)}km")

    print("Summary of Attempts:")
    print(car_one)
    print(car_two)
    print(car_three)


main()
