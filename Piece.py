class Piece:
    def __init__(self, id, color, y, x, is_king=False):
        self.color = color
        self.is_king = is_king
        self.y = y
        self.x = x
        self.id = id

    def crown(self):
        self.is_king = True
