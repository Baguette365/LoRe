#imports

#kivy
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


kivy.require("2.0.0")

class LoRe(App):
    def build(self):
        return MainMenu()
    
    
class MainMenu(FloatLayout):
    def __init__(self):
        super(MainMenu, self).__init__()