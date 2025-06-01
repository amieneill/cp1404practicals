"""
CP1404 - Practical_01
Program 1: Temperatures
Name: Amie Neill
"""

MENU = "Menu:\n(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"

print(MENU)
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input("Choice: ").upper()
print("Thank you.")