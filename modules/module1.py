"""Module 1."""

from numbers import Number


def f1(a: Number, b: Number) -> Number:
    """Add a and b.

    Args:
        a (Number): Some number.
        b (Number): Some number.

    Returns:
        Number: Resulting sum.
    """
    return a+b


def f2(a: Number, b: Number) -> Number:
    """Multiply a and b

    Args:
        a (Number): Some number.
        b (Number): Some number.

    Returns:
        Number: Result product.
    """
    return a*b
