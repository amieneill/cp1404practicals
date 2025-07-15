"""
CP1404 - Practical_06
Name: Amie Neill
Guitars Exercise
Estimate: 3 hours
Actual:
"""

from prac_06.guitar import Guitar


def main():
    """Run program to get and display list of guitars using Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")
        name = input("Name: ")

    maximum_name_length = max(len(guitar.name) for guitar in guitars)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>{maximum_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}")


main()
