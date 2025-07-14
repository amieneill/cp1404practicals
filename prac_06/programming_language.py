"""
CP1404 - Practical_06
Name: Amie Neill
Programming Language Exercise
Estimate: 45 minutes
Actual:
"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year=0):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if programming language is dynamic."""
        return self.typing == "dynamic"
