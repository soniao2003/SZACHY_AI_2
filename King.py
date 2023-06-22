from Piece import Piece

class King(Piece):
    PIECE_TYPE = "K"

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for dx, dy in directions:
            x = self.get_x() + dx
            y = self.get_y() + dy
            moves.append(self.get_move(board, x, y))

        return self.remove_0_from_list(moves)

    def return_piece(self):
        return King(self.get_x(), self.get_y(), self.get_color())


