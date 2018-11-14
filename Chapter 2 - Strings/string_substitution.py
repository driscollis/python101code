# string substitution

# the old way
my_string = "I like %s" % "Python"
my_string

var = "cookies"
newString = "I like %s" % var
newString


another_string = "I like %s and %s" % ("Python", var)
another_string

# this will cause a TypeError
another_string = "I like %s and %s" % "Python"

# string formatting
my_string = "%i + %i = %i" % (1,2,3)
my_string

float_string = "%f" % (1.23)
float_string

float_string2 = "%.2f" % (1.23)
float_string2

float_string3 = "%.2f" % (1.237)
float_string3

# passing bad data raises a TypeError
int_float_err = "%i + %f" % ("1", "2.00")

# this is bad too
int_float_err = "%i + %f" % (1, "2.00")

# ---------------------------
# new style of string substitution / formatting
print("%(lang)s is fun!" % {"lang":"Python"})
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})

# this one won't work!
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2})

# this is a fix of the previous example
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

# messing with the order of substitution
"Python is as simple as {0}, {1}, {2}".format("a", "b", "c")
"Python is as simple as {1}, {0}, {2}".format("a", "b", "c")

# creating the dict and then doing the substitution
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))