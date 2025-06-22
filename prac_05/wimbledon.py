"""
CP1404 - Practical_05
Name: Amie Neill
Wimbledon Exercise
Estimate: 90 minutes
Actual:
"""

filename = "wimbledon.csv"
with open(filename, "r", encoding="utf-8-sig") as in_file:
    for line in in_file:
        print(line)
