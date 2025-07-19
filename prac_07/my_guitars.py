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
    guitars = []
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))

    print("Display Guitars:")
    display_guitars(guitars)

    print("\nSorted Guitars by year:")
    guitars.sort()
    display_guitars(guitars)


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i:2}. {guitar}")


if __name__ == "__main__":
    main()
