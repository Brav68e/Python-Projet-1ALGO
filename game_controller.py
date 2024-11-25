from game import *
from submenu import *

class Game_controller():


    def __init__(self):
        
        self.menu = None
        self.game = None
        self.launch_menu()


    def launch_menu(self, root=0):
        self.menu = MainMenu(self, root)

    
    def launch_game(self, size, username1, username2, root, path):
        self.game = Game(self, size, username1, username2, root, path)