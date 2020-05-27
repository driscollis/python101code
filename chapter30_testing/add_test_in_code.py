# add_test_in_code.py

def add(a: int, b: int) -> int:
    """
    >>> add(1, 2)
    3
    >>> add(4, 5)
    9
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)