"""
CP1404 - Practical_01
Program 3: Debugging - Broken Scores
Name: Amie Neill
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
