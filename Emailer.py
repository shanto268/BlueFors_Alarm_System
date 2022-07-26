# -*- coding: utf-8 -*-
"""
===========================================
Program : LFL_Lab_Maintenance/Emailer.py
===========================================
Summary:
"""
__author__ = "Sadman Ahmed Shanto"

#libraries used
import smtplib
import datetime as time
import io
import os
import json
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

#Email vairables
load_dotenv(".env")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = 587
GMAIL_USERNAME =  os.environ.get("EMAIL_ID")
GMAIL_PASSWORD =  os.environ.get("PASSWD")



class Emailer:
    def __init__(self, email_list, text_list, subjectLine, emailContent):
        self.email_list = email_list
        self.text_list = text_list
        self.subjectLine = subjectLine
        self.emailContent = emailContent
        self.path2pdf = ""

    def send_email(self):
        destination = self.email_list
        subject = self.subjectLine
        message = self.emailContent

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        # Craft message (obj)
        msg = MIMEMultipart()

        msg['Subject'] = subject
        msg['From'] = GMAIL_USERNAME
        msg['To'] = destination
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        # send msg
        server.send_message(msg)
        server.close()

    def send_email_pdf_figs(self, path_to_pdf, subject, message, destination):
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        # Craft message (obj)
        msg = MIMEMultipart()

        # message = f'{message}\n\nSent from APDL_DAQ_Machine and Quanah.'
        msg['Subject'] = subject
        msg['From'] = GMAIL_USERNAME
        msg['To'] = destination
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        with open(path_to_pdf, "rb") as f:
            #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
            attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header('Content-Disposition',
                          'attachment',
                          filename=str(path_to_pdf))
        msg.attach(attach)
        # send msg
        server.send_message(msg)
        server.close()

    def sendtext(self):
        recipient=self.email_list
        subject=self.subjectLine
        content=self.emailContent
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.starttls()
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject + "\n"
        body = content + "\n"
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        session.sendmail(GMAIL_USERNAME, recipient, sms)
        session.quit

    def alert(self):
        emails = self.email_list
        for email in emails:
            print("Emailing {}".format(email))
            self.send_email()
