"""
CP1404 - Practical_07
Name: Amie Neill
More Guitars Exercise
"""

import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """DOCSTRING TBA."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))

    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


if __name__ == "__main__":
    main()
