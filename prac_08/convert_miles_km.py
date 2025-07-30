"""
CP1404 - Practical_08
Name: Amie Neill
Miles to Kilometres Converter
Estimate: 3 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometresConverterApp(App):
    """Kivy App that converts miles to kilometres."""
    def build(self):
        """Build the Kivy app GUI using kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometresConverterApp().run()
