import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK

    def is_taken(self, x, y):
        pass
