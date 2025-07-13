"""
CP1404 - Practical_05
Name: Amie Neill
State Names
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

for code in CODE_TO_NAME:
    print(f"{code:3} is {CODE_TO_NAME[code]}")

is_valid_input = False
while not is_valid_input:
    state_code = input("Enter short state: ").upper()
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        is_valid_input = True
    except KeyError:
        print("Invalid short state")