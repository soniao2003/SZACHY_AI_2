from Piece import Piece

class Bishop(Piece):

    PIECE_TYPE = "B"

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        return Piece.get_possible_diagonal_moves(self, board)

    def return_piece(self):
        return Bishop(self.get_x(), self.get_y(), self.get_color())
