def add(x, y):
    return x + y

def division(x, y):
    return x / y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    import sys
    print(sys.argv)
    v = sys.argv[1].lower()
    valOne = int(sys.argv[2])
    valTwo = int(sys.argv[3])
    if v == "a":
        print(add(valOne, valTwo))
    elif v == "d":
        print(division(valOne, valTwo))
    elif v == "m":
        print(multiply(valOne, valTwo))
    elif v == "s":
        print(subtract(valOne, valTwo))
    else:
        pass