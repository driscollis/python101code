# create_database.py

import sqlite3

# use :memory: to put it in RAM
conn = sqlite3.connect("books.db")

cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE books
                  (title text, author text, release_date text,
                   publisher text, book_type text)
               """)