from src.calculator import add, divide, subtract


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_subtract():
    assert subtract(5, 2) == 3
