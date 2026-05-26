import enum
from collections.abc import Iterator


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


# orthogonal neighbor offsets up down left right diagonals do not count
_ORTHOGONAL_OFFSETS = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Goban:
    def __init__(self, goban: list[str]) -> None:
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
        check whether the stone at a given position is taken

        a stone is taken when its connected same color shape has no liberty
        runs in linear time over the board each stone is visited once

        args
            x the x coordinate
            y the y coordinate

        returns
            true if the stone is taken false otherwise
        """
        # if there is no stone here there is nothing to take so return false
        if self.get_status(x, y) not in (Status.BLACK, Status.WHITE):
            return False

        # the stone is taken when its group has no free space next to it
        return not self._has_liberty(self._shape_at(x, y))

    def _neighbors(self, x: int, y: int) -> Iterator[tuple[int, int]]:
        """yield the four ortogonal neighbors of x y diagonals do not count"""
        # give back the cells above below left and right of x y
        for dx, dy in _ORTHOGONAL_OFFSETS:
            yield x + dx, y + dy

    def _shape_at(self, x: int, y: int) -> set[tuple[int, int]]:
        """collect every stone connected to x y that shares its color

        iterative flood fill to avoid recursion limits on large bords
        """
        # the color of the group we are looking for
        color = self.get_status(x, y)
        # stones we already added to the group we also use this to not visit twice
        shape: set[tuple[int, int]] = set()
        # stones we still need to check
        to_visit = [(x, y)]

        while to_visit:
            pos = to_visit.pop()
            # skip if we have seen this stone already
            if pos in shape:
                continue
            shape.add(pos)
            # add neighbours of the same color that we have not seen yet
            to_visit.extend(
                n
                for n in self._neighbors(*pos)
                if n not in shape and self.get_status(*n) == color
            )

        return shape

    def _has_liberty(self, stones: set[tuple[int, int]]) -> bool:
        """true if any stone of the shape touches an empty point

        board edges out are not libertis so they are simply ignored here
        """
        # true as soon as we find one empty cell next to any stone of the grup
        return any(
            self.get_status(nx, ny) == Status.EMPTY
            for x, y in stones
            for nx, ny in self._neighbors(x, y)
        )

if __name__ == "__main__":
    demo = Goban([
        ".#.",
        "#o#",
        ".#.",
    ])
    print("board")
    for row in demo.goban:
        print(row)
    print("white stone at 1 1 taken", demo.is_taken(1, 1))
