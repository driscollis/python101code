# iterating_over_cells.py

from openpyxl import load_workbook

def iterating_range(path):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    for cell in sheet['A']:
        print(cell)

if __name__ == '__main__':
    iterating_range('books.xlsx')