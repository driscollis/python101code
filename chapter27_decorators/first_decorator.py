

def func_info(func):
    def wrapper():
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        result = func()
        return result
    return wrapper


def treble():
    return 3 * 3

decorator = func_info(treble)
print(decorator())
