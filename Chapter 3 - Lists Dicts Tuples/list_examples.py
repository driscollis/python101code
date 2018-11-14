# two ways to create an empty list
my_list = []
my_list = list()

# examples of lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

# create a nested list
my_nested_list = [my_list, my_list2]

# combine / extend a list
combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)

# or just concatenate the lists together
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2

# sort a list
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
alpha_list

# finding a logic error
alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
# the sort method returns a None object as lists sort in-place
print(sorted_list)