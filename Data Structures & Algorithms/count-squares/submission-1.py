
from collections import defaultdict, Counter
from typing import List

class CountSquares:

    def __init__(self):
        # point frequency: (x, y) → count
        self.pts = Counter()
        # for fast lookup of all y's that exist for a given x
        self.x_map = defaultdict(Counter)   # x → Counter of y's

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts[(x, y)] += 1
        self.x_map[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        # iterate over every point that has the same x
        for y2, cnt in self.x_map[x].items():
            if y2 == y:
                continue                          # same point → side length 0

            d = y2 - y                            # can be positive or negative

            # square to the right
            ans += cnt * self.pts[(x + d, y)] * self.pts[(x + d, y2)]

            # square to the left
            ans += cnt * self.pts[(x - d, y)] * self.pts[(x - d, y2)]

        return ans