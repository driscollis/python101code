# open a file in read-only mode
handle = open("test.txt", "r")
# read the data
data = handle.read()
# print it out
print(data)
# close the file
handle.close()