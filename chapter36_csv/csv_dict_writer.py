# csv_dict_writer.py

import csv

def csv_dict_writer(path, headers, data):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',',
                                fieldnames=headers)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

if __name__ == '__main__':
    data = '''book_title,author,publisher,pub_date,isbn
    Python 101,Mike Driscoll, Mike Driscoll,2020,123456789
    wxPython Recipes,Mike Driscoll,Apress,2018,978-1-4842-3237-8
    Python Interviews,Mike Driscoll,Packt Publishing,2018,9781788399081'''
    records = []
    for line in data.splitlines():
        records.append(line.strip().split(','))
    headers = records.pop(0)

    list_of_dicts = []
    for row in records:
        my_dict = dict(zip(headers, row))
        list_of_dicts.append(my_dict)

    csv_dict_writer('output_dict.csv', headers, list_of_dicts)