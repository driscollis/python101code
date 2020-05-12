# decorator_syntax.py

def func_info(func):
    def wrapper(*args):
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        result = func(*args)
        return result
    return wrapper

@func_info
def treble(a: int) -> int:
    """A function that triples its input"""
    return a * 3

print(treble(5))
