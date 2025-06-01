"""
CP1404 - Practical_02
Password Check Program
Name: Amie Neill
"""

minimum_password_length = 10
password = input("Password: ")
while len(password) < minimum_password_length:
    print("Password too short")
    password = input("Password: ")

print('*' * len(password))