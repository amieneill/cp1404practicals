"""
CP1404 - Practical_09
Taxi Simulator Exercise
Name: Amie Neill
"""

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice != "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option.")
        print(MENU)
        choice = input(">>>").lower()


if __name__ == '__main__':
    main()
