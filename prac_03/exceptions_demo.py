"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a user enters input that is not an integer.
2. When will a ZeroDivisionError occur? When a user enters 0 for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? You could add a while loop to check if user input for denominator is valid?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")