"""Minimal linear regression helper for the homework.

This file provides a simple implementation of ordinary least squares for a
single-feature linear regression (y = a * x + b). The implementation is kept
compact and well-tested to be suitable for classroom assignments.
"""
from typing import Iterable, Tuple


def fit_linear_regression(x: Iterable[float], y: Iterable[float]) -> Tuple[float, float]:
    """Fit slope and intercept for y = a * x + b using OLS.

    Returns (a, b).

    Raises ValueError if inputs have different lengths or have fewer than 2
    observations.
    """
    xs = list(x)
    ys = list(y)
    if len(xs) != len(ys):
        raise ValueError("x and y must have the same length")
    n = len(xs)
    if n < 2:
        raise ValueError("Need at least two observations to fit linear regression")

    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(xs, ys))
    den = sum((xi - mean_x) ** 2 for xi in xs)
    if den == 0:
        raise ValueError("Cannot fit linear regression when all x are equal")
    a = num / den
    b = mean_y - a * mean_x
    return a, b


def predict(x: Iterable[float], a: float, b: float) -> list:
    """Predict y values for inputs x given slope a and intercept b."""
    return [a * xi + b for xi in x]
