# Given an array of non-negative integers that represent the bars (y value) in a
# histogram (with the array index being the x value), find the rectangle with the largest
# area under the curve and above the x-axis (i.e. the largest rectangle that fits inside the
# histogram). Return the pair of array indices that represent the rectangle.
# * Test Cases
# Note that there may be other valid answers.
# For array [2,4,2,1], the largest area is 6, with height 2, and width from indices 0 to 2:
# For array [2,4,2,1,10,6,10] the largest area is 18, with height 6 and width from
# indices 4 to 6.

import math
from typing import List
import unittest


def find_minimum(values: List[int]) -> int:
    """Return the index of the minimum element."""
    index = -1
    minimum = float("inf")
    for i, n in enumerate(values):
        if n < minimum:
            index = i
            minimum = n
    return index


def maximum_rectangle(histogram: List[int]) -> int:
    """Find the area of the maximum rectangle under the curve."""
    if not histogram:
        return 0
    if len(histogram) == 1:
        return histogram[0]
    index = find_minimum(histogram)
    return max(
        maximum_rectangle(histogram[:index]),
        histogram[index] * len(histogram),
        maximum_rectangle(histogram[index + 1 :]),
    )   

if __name__ == "__main__":
    histogram = [2,4,2,1,10,6,10]
    print(maximum_rectangle(histogram))
    unittest.main()