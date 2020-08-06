# csv_writer_rows.py

import csv

def csv_writer(path, data):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

if __name__ == '__main__':
    data = '''book_title,author,publisher,pub_date,isbn
    Python 101,Mike Driscoll, Mike Driscoll,2020,123456789
    wxPython Recipes,Mike Driscoll,Apress,2018,978-1-4842-3237-8
    Python Interviews,Mike Driscoll,Packt Publishing,2018,9781788399081'''
    records = []
    for line in data.splitlines():
        records.append(line.strip().split(','))
    csv_writer('output2.csv', records)