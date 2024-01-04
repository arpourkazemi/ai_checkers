class Piece:
    def __init__(self, id, color, y, x, isKing=False):
        self.color = color
        self.isKing = isKing
        self.y = y
        self.x = x
        self.id = id

    def crown(self):
        self.king = True
