"""
CP1404 - Practical_02
Password Check Program
Name: Amie Neill
"""


def main():
    """Run password check program."""
    minimum_password_length = 10
    password = get_password(minimum_password_length)
    print_asterisks(password)


def get_password(minimum_password_length):
    """Get password and validate length."""
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print("Password too short")
        password = input("Password: ")
    return password


def print_asterisks(password):
    """Print asterisks based on password length."""
    print('*' * len(password))


main()
