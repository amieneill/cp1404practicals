"""
CP1404 - Practical_05
Name: Amie Neill
Emails Exercise
Estimate: 45 minutes
Actual:
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        response = input(f"Is your name {name}? (y/n): ")
        if response != "y" and response != "":
            name = input("Name: ")
        email_to_name[email] = name
        print(f"Name: {name} ({email})")
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    at_symbol = email.split("@")[0]
    parts = at_symbol.split(".")
    name = " ".join(parts).title()
    return name


main()