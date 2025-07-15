"""
CP1404 - Practical_06
Name: Amie Neill
Guitars Exercise
Estimate: 3 hours
Actual:
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2025


def main():
    """Run and test Guitar class get_age() and is_vintage() methods."""

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 666)

    print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False Got {another_guitar.is_vintage()}")


main()
