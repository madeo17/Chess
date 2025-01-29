from .piece import Piece


class Rook(Piece):
    def __init__(self, is_white: bool):
        super().__init__("rook", is_white)

    def get_line(self, square, direction: str) -> list:
        """
        Get straight line from a given direction with possible destinations
        :param square: starting square
        :param direction: left, right, up or down
        :return: list of squares
        """
        if next_square := square.neighbor[direction]:
            if not next_square.has_piece():
                return [next_square] + self.get_line(next_square, direction)
            else:
                if next_square.piece.is_same_side(self):
                    return []
                return [next_square]
        return []

    def get_possible_destinations(self, current_square):
        result = []
        for direction in ("left", "up", "right", "down"):
            result += self.get_line(current_square, direction)
        return result
