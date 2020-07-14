# simple_table.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

def simple_table():
    doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
    flowables = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tbl = Table(data)
    flowables.append(tbl)

    doc.build(flowables)

if __name__ == '__main__':
    simple_table()