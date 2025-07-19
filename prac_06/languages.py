"""
CP1404 - Practical_06
Name: Amie Neill
Language Exercise
Estimate: 45 minutes
Actual: 1.5 hours
"""

from programming_language import ProgrammingLanguage


def main():
    """List and print programming language details."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
