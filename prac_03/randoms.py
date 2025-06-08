"""
CP1404 - Practical_03
Random Numbers Program
Name: Amie Neill
"""

import random

print(random.randint(5, 20))  # line 1
# Output is a random integer between 5 and 20
# Smallest number: 5
# Largest number: 20

print(random.randrange(3, 10, 2))  # line 2
# Output is a random number between 3 and 9, with a step of 2
# Smallest number: 3
# Largest number: 9
# No, line 2 would not be able to produce a 4
# In this case it'll only produce an odd number in range

print(random.uniform(2.5, 5.5))  # line 3
# Output is a random float between 2.5 and 5.5
# Smallest number: 2.5
# Largest number: 5.5

# Produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)
