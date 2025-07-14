"""
CP1404 - Practical_06
Name: Amie Neill
Guitars Exercise
Estimate: 3 hours
Actual:
"""
CURRENT_YEAR = 2025


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year
