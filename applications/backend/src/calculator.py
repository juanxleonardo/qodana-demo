def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    return a / b


def unused_helper(items: list) -> list:
    result = []
    for item in items:
        if item != None:
            result.append(item)
    return result
