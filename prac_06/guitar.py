"""
CP1404 - Practical_06
Name: Amie Neill
Guitar Exercise
Estimate: 3 hours
Actual: 4 hours
"""
CURRENT_YEAR = 2025


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar's details."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Return the age of the guitar using the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (i.e., 50 or more years old)."""
        return self.get_age() >= 50
