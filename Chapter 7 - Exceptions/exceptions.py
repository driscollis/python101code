# raise a ZeroDivisionError exception
try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
    
# this is known as a "bare except"
try:
    1 / 0
except:
    print("You cannot divide by zero!")
    
# let's raise a KeyError
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")
    
# now let's raise an IndexError
my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")
    
# the following shows how to catch multiple exceptions
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
    
# here's a shorter method of catching multiple exceptions
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")
    
# here is an example of the "finally" statement
# note: the statement following finally always runs
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
    
# here we learn how to use the "else" statement
# note: else only runs when no errors occur
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
    
# this last example demonstrates both else and finally
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")