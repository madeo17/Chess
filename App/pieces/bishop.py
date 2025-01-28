from .piece import Piece

class Bishop(Piece):
    def __init__(self, is_white: bool):
        super().__init__("bishop", is_white)

    def get_diagonal(self, square, horizontal: str, vertical: str) -> list:
        """
        Get diagonal with possible destinations
        :param square: starting square
        :param horizontal: left or right
        :param vertical: up or down
        :return: list of squares
        """
        if square.neighbor[horizontal] and (next_square := square.neighbor[horizontal].neighbor[vertical]):
            if not next_square.has_piece():
                return [next_square] + self.get_diagonal(next_square, horizontal, vertical)
            else:
                if next_square.piece.is_same_side(self):
                    return []
                else:
                    return [next_square]
        else:
            return []

    def get_possible_destinations(self, current_square):
        result = []
        for horizontal in ("left", "right"):
            for vertical in ("up", "down"):
                result += self.get_diagonal(current_square, horizontal, vertical)
        return result
