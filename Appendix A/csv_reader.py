import csv

def read_csv(path):
    """"""
    try:
        with open(path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                name, email = line
                print(name)
                print(email)
    except IOError:
        print("Error reading file: %s" % path)
        raise

if __name__ == "__main__":
    path = "backers.csv"
    read_csv(path)