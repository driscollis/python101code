# open a file that is in the same folder as this script
handle = open("test.txt")

# open a file by specifying its path
handle = open(r"C:\Users\mike\py101book\data\test.txt", "r")

# open the file in read-only binary mode
handle = open("test.pdf", "rb")