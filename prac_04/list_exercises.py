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
