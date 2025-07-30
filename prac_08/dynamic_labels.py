"""
CP1404 - Practical_08
Name: Amie Neill
Dynamic Labels
Estimate: 2 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Kivy App that displays dynamic labels for names in a list."""
    def build(self):
        """Build the Kivy App GUI using kv file."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Archer", "Sia", "Charlie", "Kass", "Willow"]
        return self.root


DynamicLabelsApp().run()
