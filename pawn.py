class Pawn():

    def __init__(self, value, owner, coord):
        
        self.value = value                  # rook = 1, queen = 2
        self.owner = owner                  # Object of Player type
        self.coord = coord                  # Tuple/List of coordinates (row/column)


    def get_coord(self):
        return self.coord
    
    def set_coord(self, value):
        self.coord = value

    
    def get_value(self):
        return self.value
    
    
    def get_owner(self):
        return self.owner