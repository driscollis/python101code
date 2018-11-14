# create a function with defaults
def keyword_function(a=1, b=2):
    return a+b

# call it with keyword arguments
keyword_function(b=4, a=5)

# call the function without arguments (i.e. use the defaults)
keyword_function()