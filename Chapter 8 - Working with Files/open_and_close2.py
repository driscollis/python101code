handle = open("test.txt", "r")
data = handle.readline() # read just one line
print(data)
handle.close()