"""
CP1404 - Practical_02
Temperatures Program
Name: Amie Neill
"""


def main():
    """Run temperatures program."""

    menu = "Menu:\n(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"

    print(menu)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input("Choice: ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


main()
