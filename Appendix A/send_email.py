import os
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

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
    
if __name__ == "__main__":
    send_email("mike@example.org", "output/python101.pdf")