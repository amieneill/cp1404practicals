"""
CP1404 - Practical_04
Name: Amie Neill
List Exercises
"""

# Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"First number: {numbers[0]}")
print(f"Last number: {numbers[-1]}")
print(f"Smallest number: {min(numbers)}")
print(f"Largest number: {max(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

