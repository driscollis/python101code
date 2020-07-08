# delete_record.py

import sqlite3

def delete_author(author):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    sql = f"""
    DELETE FROM books
    WHERE author = '{author}'
    """
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':
    delete_author(author='Al Sweigart')