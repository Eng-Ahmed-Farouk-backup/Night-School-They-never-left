from entities import *
from items import *
from interactive_console import *
import sys

class Game:
    def __init__(self):
        self.player = Player("Hero", 100, 10, 5, 0, 0.15)
        self.settings = {
            "difficulty": "Normal",
            "text_speed": "Normal",
            "sound_volume": 5
        }
    
    def menu(self):
        options = ["Start Game", "Settings", "Exit"]
        option = interactive_menu(options, "Welcome to the RPG Game!", "yellow")
        if option == 0:
            self.start_game()
        elif option == 1:
            self.settings_menu()
        elif option == 2:
            println("Thanks for playing!", "yellow")
            sys.exit()
    
    def settings_menu(self):
        options = ["Difficulty", "Text Speed", "Music Volume", "Back"]
        while True:
            option = interactive_menu(options, "Settings", "yellow")
            if option == 0:
                self.difficulty_menu()
            elif option == 1:
                self.text_speed_menu()
            elif option == 2:
                self.sound_volume_menu()
            elif option == 3:
                return
    
    def difficulty_menu(self):
        options = ["Easy", "Normal", "Hard", "Back"]
        option = interactive_menu(options, "Select Difficulty", "yellow")
        if option == 0:
            self.settings["difficulty"] = "Easy"
        elif option == 1:
            self.settings["difficulty"] = "Normal"
        elif option == 2:
            self.settings["difficulty"] = "Hard"
        elif option == 3:
            return
    
    def text_speed_menu(self):
        options = ["Slow", "Normal", "Fast", "Back"]
        option = interactive_menu(options, "Select Text Speed", "yellow")
        if option == 0:
            self.settings["text_speed"] = "Slow"
        elif option == 1:
            self.settings["text_speed"] = "Normal"
        elif option == 2:
            self.settings["text_speed"] = "Fast"
        elif option == 3:
            return
