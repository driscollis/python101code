handle = open("test.txt", "r")
for line in handle:
    print(line)
handle.close()