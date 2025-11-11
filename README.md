# Goban Technical Test

This repository contains the same technical test implemented in two languages: Python and Java.

## Goal
Implement a method that determines whether the stone at position `x, y` on a goban (Go board) is taken (i.e. the entire shape it belongs to has no liberties).

## Vocabulary
- **Goban**: the board on which stones are placed.
- **Shape**: one or more orthogonally adjacent stones (`up`, `down`, `left`, `right`) of the same color. Diagonals do not count.
- **Liberty**: an empty point orthogonally adjacent to any stone in a shape.

## Rules Recap
1. The goban size is arbitrary (handled by the provided data structure).
2. Two players: Black (`#`) and White (`o`).
3. Stones are placed one per turn; positions outside the provided grid are considered `OUT`.
4. A shape is taken when it has no liberties.

## Task
Write the function that returns whether the stone at `(x, y)` is taken:
- Python: implement `Goban.is_taken(self, x, y)` in `python/goban.py`.
- Java: implement `Goban.isTaken(int x, int y)` in `java/src/main/java/com/example/goban/Goban.java`.

You may add helper functions / parameters if needed while keeping clear, idiomatic code.

Use the provided status accessors:
- Python: `get_status(x, y)` returns `Status.BLACK`, `Status.WHITE`, `Status.EMPTY`, or `Status.OUT`.
- Java: `getStatus(x, y)` returns the equivalent `Status` enum values.

Return `True` / `true` only if the stone exists at `(x, y)` and the entire connected shape of that color has zero liberties.

## Examples
```
# = black
o = white
. = empty

.#.
#o#    <= o is taken: no adjacent empty points
.#.

...
#o#    <= o is not taken: liberty above
.#.

o#    <= o is taken: top and left are OUT (not liberties)
#.

oo.
##o    <= black shape (#) is taken: no liberties
o#o
.o.

oo.
##.    <= black shape (#) is not taken: liberty at x=2, y=1 (0,0 top-left)
o#o
.o.
```

## Running Tests
### Python
From repository root:
```
git clone https://github.com/lumapps/test-goban.git
cd test-goban
python3 -m venv venv
source venv/bin/activate
pip install -r python/requirements.txt
pytest python
```
(Or activate the venv and run `pytest .` from inside `python/`.)

### Java
From repository root:
```
cd java
./gradlew test
```
(First clone and enter the repository if you have not already.)

## Files of Interest
- Python implementation: `python/goban.py`
- Python tests: `python/test_goban.py`
- Java implementation: `java/src/main/java/com/example/goban/Goban.java`
- Java tests: `java/src/test/java/com/example/goban/GobanTest.java`

Focus only on implementing the capture logic; no additional features required.
