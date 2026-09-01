import os


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def append_to(value, items=[]):
    items.append(value)
    return items


def divide(a: int, b: int) -> float:
    return a / b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def unused_helper(items: list) -> list:
    result = []
    for item in items:
        if item != None:
            result.append(item)
    return result
