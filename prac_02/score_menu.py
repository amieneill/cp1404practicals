"""
CP1404 - Practical_02
Scores Menu Program
Name: Amie Neill
"""

MENU = "Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
print(MENU)

choice = input("Choice: ").upper()
while choice != 'Q':
    if choice == 'G':
        pass
    elif choice == 'P':
        pass
    elif choice == 'S':
        pass
    else:
        print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").upper()
print("Farewell")





