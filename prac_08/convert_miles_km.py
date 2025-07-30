"""
CP1404 - Practical_08
Name: Amie Neill
Miles to Kilometres Converter
Estimate: 3 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRES = 1.60934


class MilesToKilometresConverterApp(App):
    """Kivy App that converts miles to kilometres."""
    km_output = StringProperty()

    def build(self):
        """Build the Kivy app GUI using kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Handle miles to kilometre conversion."""
        print('handle conversion')
        try:
            miles = float(text)
            self.km_output = str(miles * MILES_TO_KILOMETRES)
        except ValueError:
            self.km_output = "Invalid input"

    def handle_increment(self, text, change):
        """Handle Up/Down buttons current miles value by +1 or -1."""
        print('handle_increment')
        miles = float(text)
        miles = miles + change
        self.root.ids.input_miles.text = str(miles)
        self.km_output = str(miles * MILES_TO_KILOMETRES)



MilesToKilometresConverterApp().run()
