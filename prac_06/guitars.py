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
        year = get_valid_year()
        cost = get_valid_cost()
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    maximum_name_length = max(len(guitar.name) for guitar in guitars)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>{maximum_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

def get_valid_cost():
    """Get valid input for guitar cost."""
    cost = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            cost = float(input("Cost: $"))
            if cost < 0:
                print("Cost must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input.")
    return cost


def get_valid_year():
    """Get valid input for guitar year."""
    year = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            year = int(input("Year: "))
            if year < 0:
                print("Year must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input.")
    return year


main()
