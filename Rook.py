from Piece import Piece

class Rook(Piece):

    PIECE_TYPE = "R"

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def return_piece(self):
        return Rook(self.get_x(), self.get_y(), self.get_color())
