import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        self.title = "What's This?"
        return Label(text="Hello world")


if __name__ == "__main__":
    MyApp().run()
    print()
