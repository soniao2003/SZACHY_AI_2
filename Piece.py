from Move import Move

class Piece():

    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def get_piece_type(self):
        return self.piece_type

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    #metoda zwraca move z koordynatami starymi i nowymi pionka, który się rusza, sprawdzenie czy koordynaty są na planszy i czy na polu nie ma naszego pionka
    def get_move(self, board, xto, yto):
        move = 0
        if (board.on_board(xto, yto)):
            piece = board.get_piece(xto, yto)
            if (piece != 0):
                if (piece.color != self.get_color()):
                    move = Move(self.get_x(), self.get_y(), xto, yto)
            else:
                move = Move(self.get_x(), self.get_y(), xto, yto)
        return move

    # zwraca listę bez 0
    def remove_0_from_list(self, list):
        return [move for move in list if move != 0]

    def to_string(self):
        return self.get_color() + self.get_piece_type() + " "

    @staticmethod
    def get_possible_diagonal_moves(self, board):
        moves = []

        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for direction in directions:
            (x, y) = (self.x, self.y)
            (dx, dy) = direction

            while True:
                x += dx
                y += dy

                if not board.on_board(x, y):
                    break

                piece = board.get_piece(x, y)
                moves.append(self.get_move(board, x, y))

                if piece != 0:
                    break

        return self.remove_0_from_list(moves)
    @staticmethod
    def get_possible_horizontal_moves(self, board):
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            (dx, dy) = direction
            (x, y) = (self.get_x(), self.get_y())

            while True:
                x += dx
                y += dy

                if not board.on_board(x, y):
                    break

                piece = board.get_piece(x, y)
                moves.append(self.get_move(board, x, y))

                if piece != 0:
                    break

        return self.remove_0_from_list(moves)


