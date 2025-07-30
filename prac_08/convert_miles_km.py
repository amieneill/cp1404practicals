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
        miles = self.handle_input(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle Up/Down buttons current miles value by +1 or -1."""
        print('handle_increment')
        miles = self.handle_input(text) + change
        self.root.ids.input_miles.text = str(miles)
        self.update_result(miles)

    def update_result(self, miles):
        """Update the kilometre output label based on the mile value."""
        print('display result')
        self.km_output = str(miles * MILES_TO_KILOMETRES)

    def handle_input(self, text):
        """Convert text to a float. Return 0.0 if the input is invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometresConverterApp().run()
