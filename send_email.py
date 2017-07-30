#!/usr/bin/env python
import sys
import smtplib


GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

GMAIL_EMAIL = "lollerbladesunicornmagic@gmail.com"
GMAIL_PASSWORD = "whatwhat"


def initialize_smtp_server():
    """
    Initialize and greet SMTP server using provided credentials.
    Return SMTP server object.
    """
    smtp_server = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
    return smtp_server


def send_email(email):
    to_email = email
    from_email = GMAIL_EMAIL
    subj = "Thank you for being an active commenter"
    header = "To:%s\nFrom:%s\nSubject:%s \n" % (to_email, from_email, subj)

    msg_body = """
    Hi %s,

    Thank you very much for your repeated comments on our service.
    The interaction is much appreciated.

    Thank you!""" % email

    content = header + "\n" + msg_body

    smtp_server = initialize_smtp_server()
    smtp_server.sendmail(from_email, to_email, content)
    smtp_server.close()


if __name__ == "__main__":
    for email in sys.stdin.readlines():
        email = email.strip()
        send_email(email)

