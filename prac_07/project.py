"""
CP1404 - Practical_07
Name: Amie Neill
Project Management Program
Estimate: 6 hours
Actual:
"""


class Project:
    """Represents a Project object."""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
