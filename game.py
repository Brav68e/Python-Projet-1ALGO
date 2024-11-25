from player import *
from pawn import *
from tkinter import *
from tkinter import messagebox


class Game():

    def __init__(self, controller, root, size, username1, username2, path):

        self.controller = controller
        
        self.selected_pawn = None
        self.possibilities = []

        if path:
            self.load_game(path)
            print(self.board)
        else:
            self.size = size
            self.players = [Player(username1, (size-1, 0), size**2 // 4), Player(username2, (0, size-1), size**2 // 4)]
            self.current_player = self.players[0]
            self.current_player_index = 0
            self.create_board(size)


        #GUI part
        self.root = root
        #Destroy every child
        for el in self.root.winfo_children():
            el.destroy()

        #General settings
        self.root.title("Game")
        self.root.geometry("900x900")
        self.root.resizable(False, False)
        self.canvas_size = 800              #Only handling 'square' size

        self.canvas = Canvas(self.root, height=self.canvas_size, width=self.canvas_size)
        self.canvas.pack(side=TOP)

        self.text = Label(self.root, text=f"Turn of : {self.current_player.get_username()}", font= 25)
        self.text.pack(side=BOTTOM, pady=20)

        self.refresh()

        #Binding, this act as the event handler -> "mainloop"
        self.canvas.bind("<Button-1>", self.interact)


        self.root.mainloop()


##################################################################################


    def create_board(self, size):
        '''Init a board of size n'''

        #Initialisation of the board
        self.board = [[0 for i in range(size)] for j in range(size)]

        #Place pawn for each player
        #Starting of with player 1 :
        for line in range(size//2, size):
            for column in range(size//2):
                if line==size-1 and column==0 :     #Queen for player 1
                    self.board[line][column] = Pawn(2, self.players[0], (line, column))
                else:
                    self.board[line][column] = Pawn(1, self.players[0], (line, column))

        #Now doing it for the other player
        for line in range(size//2):
            for column in range(size//2, size):
                if line==0 and column==size-1 :     #Queen for player 2
                    self.board[line][column] = Pawn(2, self.players[1], (line, column))
                else:
                    self.board[line][column] = Pawn(1, self.players[1], (line, column))


##################################################################################


    def load_game(self, path):

        save = open(path, "r")
        player1 = Player(save.readline())
        player2 = Player(save.readline())
        self.size = int(save.readline())
        
        self.players = [player1, player2]
        self.current_player_index = int(save.readline())
        self.current_player = self.players[self.current_player_index]

        #Now read the file and create the board
        self.board = []

        for line in range(self.size):
            current_row = []
            current_line = save.readline()

            for column, car in enumerate(current_line):
                match car:
                    case "0":
                        current_row.append(0)
                    case "1":
                        current_row.append(Pawn(1, player1, (line, column)))
                        player1.set_pawnNbr(player1.get_pawnNbr() + 1)
                    case "2":
                        current_row.append(Pawn(2, player1, (line, column)))
                        player1.set_pawnNbr(player1.get_pawnNbr() + 1)
                        player1.set_queenCoord((line, column))
                    case "3":
                        current_row.append(Pawn(1, player2, (line, column)))
                        player2.set_pawnNbr(player1.get_pawnNbr() + 1)
                    case "4":
                        current_row.append(Pawn(2, player2, (line, column)))
                        player2.set_pawnNbr(player1.get_pawnNbr() + 1)
                        player2.set_queenCoord((line, column))

            self.board.append(current_row)

        save.close()


##################################################################################


    def draw_board(self):
        '''Draw every Tiles on the canvas NOT the pawn'''

        self.tile_size = self.canvas_size/self.size

        for line in range(self.size):
            line = line*self.tile_size +2             # +2 stand for a visual issue
            for column in range(self.size):
                column = column*self.tile_size +2
                
                self.canvas.create_rectangle(column, line, column+self.tile_size, line+self.tile_size, outline="black", width=2)


##################################################################################        

    def draw_pawns(self):
        '''Draw every pawn on the board'''

        for line in range(self.size):
            for column in range(self.size):
                #Check if the tile is a pawn
                if isinstance(self.board[line][column], Pawn):
                    
                    current_pawn = self.board[line][column]
                    self.draw_pawn(current_pawn)


##################################################################################


    def draw_pawn(self, pawn, size = 1, outline = "black", width = 1):
        '''Draw 1 pawn'''

        owner = pawn.get_owner()
        value = pawn.get_value()
        line, column = pawn.get_coord()

        if owner == self.players[0] and value == 1:                 #Player 1 rook
            self.create_oval(column*self.tile_size + self.tile_size/2, line*self.tile_size + self.tile_size/2, self.tile_size/3*size, "Red", outline, width)
        elif owner == self.players[0] and value == 2:               #Player 1 queen
            self.create_oval(column*self.tile_size + self.tile_size/2, line*self.tile_size + self.tile_size/2, self.tile_size/3*size, "Pink", outline, width)
        elif owner == self.players[1] and value == 1:               #Player 2 rook
            self.create_oval(column*self.tile_size + self.tile_size/2, line*self.tile_size + self.tile_size/2, self.tile_size/3*size, "Blue", outline, width)
        else:                                                       #Player 1 queen
            self.create_oval(column*self.tile_size + self.tile_size/2, line*self.tile_size + self.tile_size/2, self.tile_size/3*size, "Purple", outline, width)


##################################################################################


    def create_oval(self, x, y, r, color, outline, width):
        '''Create a circle based on his center and radius'''
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=outline, width=width)


##################################################################################


    def refresh(self):
        '''The combination of all previously handmade drawing/updating functions'''
        self.canvas.delete(ALL)
        self.draw_board()
        self.draw_pawns()
        self.text.configure(text=f"Turn of : {self.current_player.get_username()}")


##################################################################################


    def interact(self, event):
        '''Handle interactions with left-click on the canvas'''

        column = int(event.x / self.tile_size)
        line = int(event.y / self.tile_size)

        #Pawn selection
        if isinstance(self.board[line][column], Pawn) and self.selected_pawn == None and self.board[line][column].get_owner() == self.current_player:
            self.selected_pawn = self.board[line][column]
            self.draw_pawn(self.selected_pawn, outline="Green", width=5)            #Act as a refresh
            self.possible_moves()
            self.draw_possibilities()
            
        #Pawn movement
        elif (line, column) in self.possibilities:
            tmpx, tmpy = self.selected_pawn.get_coord()
            self.board[line][column] = self.selected_pawn
            self.board[line][column].set_coord((line, column))
            self.board[tmpx][tmpy] = 0
            
            if self.selected_pawn.get_value() == 2:
                self.current_player.set_queenCoord((line, column))

            #Remove pawns due to the move that just occur
            self.remove()

            #Switch player 
            self.current_player_index = (self.current_player_index + 1) % 2
            self.current_player = self.players[self.current_player_index]

            #Reset and refresh
            self.selected_pawn = None
            self.possibilities = []
            self.refresh()

            self.check_win()

        
        #Pawn Deselection
        else :
            self.selected_pawn = None
            self.possibilities = []
            self.refresh()
        

##################################################################################


    def possible_moves(self):
        '''Update the list of coordinates where the selected pawn can go'''
        line = self.selected_pawn.get_coord()[0]
        column = self.selected_pawn.get_coord()[1]
        self.possibilities = []

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        #If the pawn is a queen, it got extra possibilities
        if self.selected_pawn.get_value() == 2:
            directions += [(1,-1), (-1,1), (1,1), (-1,-1)]

        for i,j in directions:
            compteur = 1
            #While the x and y are valid and point a empty tile
            while (line+i*compteur < self.size and line+i*compteur >= 0) and (column+j*compteur >= 0 and column+j*compteur < self.size) and self.board[line+i*compteur][column+j*compteur] == 0:
                self.possibilities.append((line+i*compteur, column+j*compteur))
                compteur += 1


##################################################################################
        

    def draw_possibilities(self):
        '''Draw on the board an indicator of where the selected pawn can go'''
        for coord in self.possibilities:
            self.create_oval(coord[1]*self.tile_size + self.tile_size/2, coord[0]*self.tile_size + self.tile_size/2, self.size/3, "Black", "Black", 1)


##################################################################################


    def remove(self):
        '''Use to remove the opponent's rook'''
        
        q_line, q_column = self.current_player.get_queenCoord()
        line, column = self.selected_pawn.get_coord()

        #If the tile is a pawn, and the pawn is a rook own by the opponent, then ...
        #Doing this of each edge of the rectangle
        if isinstance(self.board[line][q_column], Pawn) and self.board[line][q_column].get_value() == 1 and self.board[line][q_column].get_owner() == self.players[(self.current_player_index + 1) % 2]:
            opponent = self.players[(self.current_player_index + 1) % 2]
            opponent.set_pawnNbr(opponent.get_pawnNbr() - 1)
            self.board[line][q_column] = 0

        if isinstance(self.board[q_line][column], Pawn) and self.board[q_line][column].get_value() == 1 and self.board[q_line][column].get_owner() == self.players[(self.current_player_index + 1) % 2]:
            opponent = self.players[(self.current_player_index + 1) % 2]
            opponent.set_pawnNbr(opponent.get_pawnNbr() - 1)
            self.board[q_line][column] = 0


##################################################################################


    def check_win(self):
            '''Check if a player has won the game'''
            if self.current_player.get_pawnNbr() <= 2:
                if messagebox.askyesno("Game Over", f"{self.players[(self.current_player_index + 1) % 2].get_username()} has won the game !\nDo you want to play again ?"):
                    #Launch back the menu
                    self.controller.launch_menu(self.root)
                else:
                    self.root.destroy()


##############################################################################################################

if __name__ == "__main__":

    Game()