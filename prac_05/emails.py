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
        at_symbol = email.split("@")[0]
        parts = at_symbol.split(".")
        name = " ".join(parts).title()
        print(f"Name: {name} ({email})")
        email = input("Email: ")


main()