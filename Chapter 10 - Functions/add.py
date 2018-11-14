def add(a, b):
    return a + b

# call the function with arguments
add(1, 2)

# call the function with the wrong number of arguments
add(1)  # causes a TypeError

# call the function with keyword arguments
add(a=2, b=3)

# assign the result to a variable
total = add(b=4, a=5)