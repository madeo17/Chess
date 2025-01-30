from App.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, is_white: bool):
        super().__init__("knight", is_white)

    def get_possible_destinations(self, current_square):
        result = []

        for direction in ("left", "right"):
            if square := current_square(direction):
                if second_square := square(direction):
                    for turn in ("up", "down"):
                        destination_square = second_square(turn)
                        if self.is_square_available(destination_square):
                            result.append(destination_square)

        for direction in ("up", "down"):
            if square := current_square(direction):
                if second_square := square(direction):
                    for turn in ("left", "right"):
                        destination_square = second_square(turn)
                        if self.is_square_available(destination_square):
                            result.append(destination_square)

        return result
