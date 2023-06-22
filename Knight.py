from Piece import Piece

class Knight(Piece):

    PIECE_TYPE = "N"

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        moves = []
        offsets = [(2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (-2, -1), (-1, -2)]

        for dx, dy in offsets:
            x = self.get_x() + dx
            y = self.get_y() + dy
            moves.append(self.get_move(board, x, y))

        return self.remove_0_from_list(moves)

    def return_piece(self):
        return Knight(self.get_x(), self.get_y(), self.get_color())
