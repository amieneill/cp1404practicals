"""
CP1404 - Practical_01
Program 4: Loops
Name: Amie Neill
"""

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number = int(input("Number of stars: "))
for i in range(number):
    print(end='*')
print()

# d.
number = int(input("Number of stars: "))
for i in range(1, number + 1):
    print(i * '*')
print()

