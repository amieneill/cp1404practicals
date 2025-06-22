"""
CP1404 - Practical_05
Name: Amie Neill
Hex Colours
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "AliceBlue": "#f0f8ff",
                  "Amaranth": "#e52b50", "Amethyst": "#9966cc",
                  "Baby Pink": "#f4c2c2", "Black Shadows": "#bfafb2",
                  "Blue Violet": "#8a2be2", "Boysenberry": "#873260",
                  "Burgundy": "#800020", "Cerulean Frost": "#6d9bc3"}

colour_name = input("Colour name: ")
while colour_name != "":
    colour_code = COLOUR_TO_CODE.get(colour_name)
    print(f"Colour: {colour_name} is {colour_code}")
    colour_name = input("Colour name: ")

