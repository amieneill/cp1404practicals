"""
CP1404 - Practical_08
Name: Amie Neill
Dynamic Labels
Estimate: 2 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App that displays dynamic labels for names in a list."""

    def build(self):
        """Build the Kivy App GUI using kv file."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Archer", "Sia", "Charlie", "Kass", "Willow"]
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a dynamic label for each name in a list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
