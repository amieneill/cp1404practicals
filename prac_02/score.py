"""
CP1404 - Practical_02
Scores Program
Name: Amie Neill
"""


def main():
    """Run scores program."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)


def determine_score_result(score):
    """Determine score based on score input."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
