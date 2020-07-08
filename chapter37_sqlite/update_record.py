# update_record.py

import sqlite3


def update_author(old_name, new_name):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    sql = f"""
    UPDATE books
    SET author = '{new_name}'
    WHERE author = '{old_name}'
    """
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':
    update_author(old_name='Mike Driscoll',
                  new_name='Michael Driscoll')