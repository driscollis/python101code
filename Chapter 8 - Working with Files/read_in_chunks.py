handle = open("test.txt", "r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break