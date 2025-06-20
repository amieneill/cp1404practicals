"""
CP1404 - Practical_04
Name: Amie Neill
Quick pick program
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks: "))
while number_of_quick_picks <= 0:
    print("Invalid input.")
    number_of_quick_picks = int(input("How many quick picks: "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
