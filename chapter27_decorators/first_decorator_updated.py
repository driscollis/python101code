# first_decorator_updated.py

def func_info(func):
    def wrapper(*args):
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        result = func(*args)
        return result
    return wrapper


def treble(a: int) -> int:
    """A function that triples its input"""
    return a * 3


my_decorator = func_info(treble)
print(my_decorator(5))
