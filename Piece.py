class Piece:
    def __init__(self, color, y, x, isKing=False):
        self.color = color
        self.isKing = isKing
        self.y = y
        self.x = x

    def crown(self):
        self.king = True
