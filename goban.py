import enum
from typing import List


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban:
    def __init__(self, goban: List[str]) -> None:
        """
        Goban must be rectangular.
        """
        self.goban = goban

    def get_status(self, x: int, y: int) -> Status:
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
        raise ValueError(f"Unknown goban value {self.goban[y][x]}")

    def is_taken(self, x: int, y: int) -> bool:
        """
        Is the stone at (x, y) position captured?

        Errors:
            ValueError: (x, y) is EMPTY or OUT. (x, y) must have a stone.

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            True if the stone or the associated group doesn't have any liberty
            False if the group has at least one liberty
        """
        color = self.get_status(x, y)
        if color == Status.OUT:
            raise ValueError(f"Out of bound (x, y) ({x}, {y})")
        if color == Status.EMPTY:
            raise ValueError(f"No stone at ({x}, {y})")
        flood_fill = self._init_flood_fill_goban()
        result = self._is_taken_rec(flood_fill, color, x, y)
        return result

    def _is_taken_rec(
        self, flood_fill: list[list[int]], color: Status, x: int, y: int
    ) -> bool:
        """
        Recursively check if the group of stone has at least one liberty.

        Args:
            flood_fill: mark already visited positions
            color: either BLACK or WHITE (else Undefined behavior)
            x: the x coordinate
            y: the y coordinate

        Returns:
            True if the stone or the associated group have at least 1 liberty,
            False if not.
        """
        status = self.get_status(x, y)
        if status == Status.OUT:
            return True
        if flood_fill[y][x]:
            flood_fill[y][x] = False
        else:
            return True
        if status == color:
            return (
                self._is_taken_rec(flood_fill, color, x - 1, y)
                and self._is_taken_rec(flood_fill, color, x + 1, y)
                and self._is_taken_rec(flood_fill, color, x, y - 1)
                and self._is_taken_rec(flood_fill, color, x, y + 1)
            )
        elif status == Status.EMPTY:
            return False
        return True

    def _init_flood_fill_goban(self) -> list[list[int]]:
        """
        Initialize the goban to recursively flood fill the checked positions.

        Errors:
            If goban is empty or unitialized.

        Returns:
            List of list filled with 0 the same size as the current goban.
        """
        return [
            [True for _ in range(len(self.goban[0]))] for _ in range(len(self.goban))
        ]
