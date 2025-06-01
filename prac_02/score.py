"""
CP1404 - Practical_02
Scores Program
Name: Amie Neill
"""

import random


def main():
    """Run scores program."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Based on your score of {score}, your result is considered {result}.")

    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Your random score is {random_score}, your result is considered {random_result}.")


def determine_score_result(score):
    """Determine result based on score input."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
