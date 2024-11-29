class Player():

    def __init__(self, username, queen_coord = None, pawn_nbr = 0):

        self.username = username
        self.queen_coord = queen_coord
        self.pawn_nbr = pawn_nbr


    
    def get_pawnNbr(self):
        return self.pawn_nbr
    

    def set_pawnNbr(self, value):
        self.pawn_nbr = value


    def get_queenCoord(self):
        return self.queen_coord
    

    def set_queenCoord(self, value):
        self.queen_coord = value


    def get_username(self):
        return self.username