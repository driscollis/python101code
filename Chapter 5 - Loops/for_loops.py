# a basic for loop
for number in range(5):
    print(number)
    
# you can also write the above like this
for number in [0, 1, 2, 3, 4]:
    print(number)
    
# this is how to loop over the keys in a dict
a_dict = {"one":1, "two":2, "three":3}
for key in a_dict:
    print(key)
    
# sort the keys before looping over them
a_dict = {1:"one", 2:"two", 3:"three"}
keys = a_dict.keys()
sorted(keys)
for key in keys:
    print(key)
    
# Let's use a conditional to print out only even numbers
for number in range(10):
    if number % 2 == 0:
        print(number)
        
# using the else statement
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")