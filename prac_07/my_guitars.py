"""
CP1404 - Practical_07
Name: Amie Neill
More Guitars Exercise
"""

import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Run program to load, display and sort a list of guitars using Guitar class."""
    guitars = load_guitars()

    print("Display Guitars:")
    display_guitars(guitars)

    print("\nSorted Guitars by year:")
    guitars.sort()
    display_guitars(guitars)

    get_new_guitars(guitars)


def get_new_guitars(guitars):
    """Get new guitars from user, append to list and save to guitars.csv."""
    new_guitars = []

    name = input("Name: ")
    while name != "":
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

        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:,.2f} added.")
        name = input("Name: ")

    for new_guitar in new_guitars:
        guitars.append(new_guitar)

    with open(FILENAME, "w") as out_file:
        writer = csv.writer(out_file)
        for new_guitar in guitars:
            writer.writerow([new_guitar.name, new_guitar.year, new_guitar.cost])


def load_guitars():
    guitars = []
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i:2}. {guitar}")


if __name__ == "__main__":
    main()
