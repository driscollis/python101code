# a simple list comprehension
x = [i for i in range(5)]

# turn a list of strings into a list of ints
x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]

# strip off all the leading or ending white space
myStrings = [s.strip() for s in myStringList]

# how to turn a list of lists into one list (flattening)
vec = [[1,2,3], [4,5,6], [7,8,9]]
flat_vec = [num for elem in vec for num in elem]

# a simple dict comprehension
print( {i: str(i) for i in range(5)} )

# swapping keys and values with a dict comprehension
my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print( {value:key for key, value in my_dict.items()} )

# turn a list into a set using a set comprehension
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}