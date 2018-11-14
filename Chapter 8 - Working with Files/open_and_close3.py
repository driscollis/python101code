handle = open("test.txt", "r")
data = handle.readlines() # read ALL the lines!
print(data)
handle.close()