# open and read the file using the with operator
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)