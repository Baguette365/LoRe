#imports

#kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


kivy.require("2.0.0")

class LoRe(App):
    def build(self):
        return MainMenu()
    
    
class MainMenu(BoxLayout):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.language = "french"
    def TranslateButtonFunction(self):
        if self.language == "french":
            self.ids.WelcomeLabel.text       = "Bienvenue sur LoRe, le système d'apprentissage pour les meilleurs des meilleurs"
            self.ids.TranslateButton.text    = "translate to english"
            self.ids.GoToMainMenuButton.text = "aller sur le menu principal"
            self.language = "english"  # switch to english
        elif self.language == "english":
            self.ids.WelcomeLabel.text       = "Welcome on LoRe, the learning system for bests of bests"
            self.ids.TranslateButton.text    = "passer en francais"
            self.ids.GoToMainMenuButton.text = "go to the main menu"
            self.language = "french"  # switch to french

    def ReturnLanguage(self):
        return self.language

    def GoToMainMenuFunction(self):
        pass