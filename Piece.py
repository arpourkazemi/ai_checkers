class Piece:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king

    def crown(self):
        self.king = True
