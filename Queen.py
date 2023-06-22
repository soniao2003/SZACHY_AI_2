from Piece import Piece

class Queen(Piece):

    PIECE_TYPE = "Q"

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        diagonal = Piece.get_possible_diagonal_moves(self, board)
        horizontal = Piece.get_possible_horizontal_moves(self, board)
        return horizontal + diagonal

    def return_piece(self):
        return Queen(self.get_x(), self.get_y(), self.get_color())

