#imports

#kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

kivy.require("2.0.0")

Vars = [0]

class LoRe(App):
    def build(self):
        sm = ScreenManager()
        
        # Ajouter les écrans
        sm.add_widget(WelcomeScreen( name = "WelcomeScreen"  ))
        sm.add_widget(SM2(           name = "SM2"            ))
        sm.add_widget(Others(        name = "Others"         ))
        sm.add_widget(RevisionSheets(name = "RevisionSheets" ))
        sm.add_widget(BlankSheet(    name = "BlankSheet"     ))
        sm.add_widget(BackBlankSheet(name = "BackBlankSheet"))
        sm.add_widget(MenuScreen(    name = "MenuScreen"     ))
        return sm
    
    
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        self.language = "french"
        super().__init__(**kwargs)
    def TranslateButtonFunction(self):
        if self.language == "french":
            self.ids.MainMenuLabel.text             = "menu principal : "
            self.ids.TranslateButton.text           = "translate to english"
            self.ids.GoToOthersButton.text          = "divers"
            self.ids.GoToRevisionsSheetsButton.text = "fiche de révisions"
            self.ids.GoToBlankSheetButton.text      = "le feuille blanche"
            self.language = "english"  # switch to english
        elif self.language == "english":
            self.ids.MainMenuLabel.text       = "main menu : "
            self.ids.TranslateButton.text     = "passer en francais"
            self.ids.GoToOthersButton.text          = "Others"
            self.ids.GoToRevisionsSheetsButton.text = "revisions sheets"
            self.ids.GoToBlankSheetButton.text      = "BlankSheet"
            self.language = "french"  # switch to french

    def ReturnLanguage(self):
        return self.language
    
class SM2(Screen):
    def __init__(self, **kwargs):
        self.language= "french"
        super().__init__(**kwargs)
    
class Others(Screen):
    def __init__(self, **kwargs):
        self.language = "french"
        super().__init__(**kwargs)
    
class RevisionSheets(Screen):
    def __init__(self, **kwargs):
        self.language = "french"
        super().__init__(**kwargs)
    
class BlankSheet(Screen):
    def __init__(self, **kwargs):
        self.language = "french"
        super().__init__(**kwargs)
    
    def GoBackSide(self):
        Vars[0] = self.ids.FrontSheet.text
        self.manager.current = "BackBlankSheet"
    


class BackBlankSheet(Screen):
    def __init__(self, **kwargs):
        self.language = "french"
        super().__init__(**kwargs)

    def Verify(self):
        self.ids.FrontLabel.text = Vars[0]

