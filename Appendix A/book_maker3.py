import csv
import os
import smtplib
import subprocess

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

chapters = ['chapter_1.rst',
            'chapter_2.rst',
            'chapter_3.rst']

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
    return pdf_path

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

def send_email(email, pdf):
    """
    Send an email out
    """
    header0 = 'Content-Disposition'
    header1 ='attachment; filename="%s"' % os.path.basename(pdf)
    header = header0, header1
    
    host = "mail.server.com"
    server = smtplib.SMTP(host)
    subject = "Test email from Python"
    to = email
    from_addr = "test@pylib.com"
    body_text = "Here is the Alpha copy of Python 101, Part I"
    
    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg["To"] = email
    
    msg.attach( MIMEText(body_text) )
    
    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(pdf, "rb") as fh:
            data = fh.read()
        attachment.set_payload( data )
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print(msg)
        
    server.sendmail(from_addr, to, msg.as_string())
    
def main(path):
    """"""
    try:
        with open(path) as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                name, email = line
                pdf = make_book(name, email)
                send_email(email, pdf)
    except IOError:
        print("Error reading file: %s" % path)
        raise
    
if __name__ == "__main__":
    main("backers.csv")