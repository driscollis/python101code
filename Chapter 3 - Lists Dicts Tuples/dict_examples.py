# there are two ways to create a Python dictionary (dict)
my_dict = {}
another_dict = dict()

# here's an example with the dict containing data
my_other_dict = {"one":1, "two":2, "three":3}

# access values in a dict
my_other_dict["one"]
my_dict = {"name":"Mike", "address":"123 Happy Way"}
my_dict["name"]

# check if a dict has a particular key
"name" in my_dict  # returns True
"state" in my_dict  # returns False

# get a view of the keys in a dict
my_dict.keys()