# decorator_class.py

class info:

    def __init__(self, arg1, arg2):
        print('running __init__')
        self.arg1 = arg1
        self.arg2 = arg2
        print('Decorator args: {}, {}'.format(arg1, arg2))

    def __call__(self, function):
        print('in __call__')

        def wrapper(*args, **kwargs):
            print('in wrapper()')
            return function(*args, **kwargs)

        return wrapper

@info(3, 'Python')
def treble(number):
    return number * 3

print(treble(5))