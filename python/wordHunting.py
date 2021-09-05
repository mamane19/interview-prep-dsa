import collections
import copy
import itertools
from typing import Iterator, List, Sequence, Set
import unittest
import util

Cell = collections.namedtuple("Cell", "x, y, letter")


class Grid:
    """A grid of letters."""

    def __init__(self):
        self._dictionary = util.Dictionary()
        self._cells = collections.defaultdict(dict)

    def __getitem__(self, x: int) -> Cell:
        return self._cells[x]

    def set(self, x: int, y: int, letter: str) -> None:
        self._cells[x][y] = Cell(x, y, letter.lower())

    def set_row(self, column_index: int, values: Sequence[str]) -> None:
        """Set the letters of an entire column in the grid."""
        for row_index, letter in enumerate(values):
            self.set(row_index, column_index, letter)

    def is_inside(self, x: int, y: int) -> bool:
        """Check whether (x, y) falls within the grid."""
        try:
            _ = self[x][y]
            return True
        except KeyError:
            return False

    def neighbors(self, x: int, y: int, visited: Set[Cell]) -> Iterator[Cell]:
        """Return all not-yet-visited contiguous cells."""
        for dx, dy in itertools.product([-1, 0, 1], repeat=2):
            # If both offsets are zero we remain at the same cell.
            if (dx, dy) == (0, 0):
                continue
            nx, ny = x + dx, y + dy
            if not self.is_inside(nx, ny):
                continue
            n = self[nx][ny]
            if n not in visited:
                yield n

    def find_words(self, x: int, y: int, prefix: str, seen: Set[Cell]) -> List[str]:
        """Form all possible words that complete `prefix` from cell (x, y)."""
        current = self[x][y]
        seen.add(current)
        # Note the copy of 'seen' that we pass down when recursing! This
        # is important: each different "parallel universe" is independent;
        # otherwise we keep the reference to the same object and modify it.
        all_words = []
        if self._dictionary.is_prefix(prefix):
            all_words.append(prefix)
        for neighbor in self.neighbors(x, y, seen):
            word = prefix + neighbor.letter
            if self._dictionary.is_prefix(word):
                all_words.extend(
                    self.find_words(neighbor.x, neighbor.y, word, copy.copy(seen))
                )
        return all_words

    def find_longest_word(self, x: int, y: int) -> str:
        """Return the longest word starting in cell (x, y)."""
        start = self[x][y]
        words = self.find_words(x, y, start.letter, set())
        # Sort before finding the maximum so that if 2+ words have the same length,
        # we return the first one lexicographically.
        words.sort()
        return max(words, key=len)

# # let's create the grid for the hours
#     hours_grid = list(itertools.chain.from_iterable(digits[int(hours)]))
#     # let's create the grid for the minutes
#     minutes_grid = list(itertools.chain.from_iterable(digits[int(minutes)]))
#     # let's create the grid for the colon
#     sep_grid = list(itertools.chain.from_iterable(digits[":"]))
#     # let's join the grids together
#     final_grid = hours_grid + sep_grid + minutes_grid
#     # join the grids together and return
#     return "".join(final_grid)
