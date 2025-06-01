"""
CP1404 - Practical_02
Scores Menu Program
Name: Amie Neill
"""


def main():
    """Run score menu program."""
    score = []
    menu = "Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    choice = input("Choice: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            determine_score_result(score)
        elif choice == 'S':
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(menu)
        choice = input("Choice: ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score from user."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Score: "))
    return score


def determine_score_result(score):
    """Determine score result."""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(f"Based on your score of {score}, your result is considered {result}.")


def print_asterisks(score):
    """Print asterisks for score."""
    print('*' * score)


main()
