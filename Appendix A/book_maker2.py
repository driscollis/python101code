import csv
import os
import subprocess

chapters = ['chapter_1.rst',
            'chapter_2.rst',
            'chapter_3.rst']

def read_chapter(chapter):
    """
    Reads a chapter and returns the stream
    """
    path = os.path.join("data", chapter)
    try:
        with open(path) as chp_handler:
            data = chp_handler.read()
    except (IOError, OSError):
        raise Exception("Unable to open chapter: %s" % chapter)
    return data

def make_book(name="Mike", email_address="test@py.com"):
    """
    Creates Python 101 book
    """
    book_path = "output/python101.rst"
    pdf_path = "output/python101.pdf"
    page_break = """
.. raw:: pdf
   
    PageBreak
    """
    footer = """
.. footer::

    Copyright |copy| 2014 by Michael Driscoll, all rights reserved.
    Licensed to %s <%s>
    
.. |copy| unicode:: 0xA9 .. copyright sign
    """ % (name, email_address)
    try:
        with open(book_path, "w") as book:
            book.write(footer + "\n")
            for chapter in chapters:
                data = read_chapter(chapter)
                book.write(data)
                book.write("\n")
                book.write(page_break + "\n")
    except:
        print("Error writing book!")
        raise
    
    cmd = [r"C:\Python27\Scripts\rst2pdf.exe",
           book_path, "-o", pdf_path]
    subprocess.call(cmd)
    
def main(path):
    """"""
    try:
        with open(path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                name, email = line
                make_book(name, email)
    except IOError:
        print("Error reading file: %s" % path)
        raise
    
if __name__ == "__main__":
    main("backers.csv")