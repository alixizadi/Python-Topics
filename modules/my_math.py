def div(a, b):
    """
    Divide two numbers.

    >>> div(10, 2)
    5.0
    >>> div(7, 3)
    2.3333333333333335
    """
    return a / b


def add(a, b):
    """
    Add two numbers.

    >>> add(2, 3)
    5
    >>> add(10, -5)
    5
    """
    return a + b


def test_div():
    assert div(10, 2) == 5.0
    assert div(7, 3) == 2.3333333333333335


def test_add():
    assert add(2, 3) == 5
    assert add(10, -5) == 5


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_div()
    test_add()
