"""Example helper module for the homework.

This module provides a small utility function used in exercises and to
ensure the autograder finds an example file.
"""

from typing import Iterable, List


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a sequence of numbers.

    Raises ValueError on empty input.
    """
    vals = list(values)
    if not vals:
        raise ValueError("mean() arg is an empty sequence")
    return sum(vals) / len(vals)
