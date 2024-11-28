from Source_files.game import *
from Source_files.submenu import *

class Game_controller():


    def __init__(self):
        
        self.menu = None
        self.game = None
        self.launch_menu()


    def launch_menu(self, root=0):
        self.menu = MainMenu(self, root)

    
    def launch_game(self, root, size = 6, username1 = "Player 1", username2 = "Player 2", path = None):
        self.game = Game(self, root, size, username1, username2, path)
