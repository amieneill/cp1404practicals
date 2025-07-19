"""
CP1404 - Practical_07
Name: Amie Neill
Project Management Program
Estimate: 6 hours
Actual:
"""

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Run Project Management Program."""
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ")
    while choice != "Q":
        if choice == "L":
            # Prompt the user for a filename to load projects from and load them.
            pass
        elif choice == "S":
            # Prompt the user for a filename to save projects to and save them.
            pass
        elif choice == "D":
            print("Incomplete projects:")
            print("Completed projects:")
            # Add incomplete projects and completed projects list, both sorted by priority.
            pass
        elif choice == "F":
            # Ask the user for a date and display only projects that start after that date, sorted by date.
            pass
        elif choice == "A":
            # Ask the user for the inputs and add a new project to memory
            pass
        elif choice == "U":
            # Add choose a project, then modify the completion % and/or priority
            pass
        print(MENU)
        choice = input(">>> ")
    # Add "Would you like to save to projects.txt?" input prompt here.
    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()
