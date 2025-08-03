"""
CP1404 - Practical_09
Name: Amie Neill
Band class Exercise
"""

class Band:
    """Represent a Band object."""
    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician playing an instrument or if they need one."""
        return "\n".join(musician.play() for musician in self.musicians)
