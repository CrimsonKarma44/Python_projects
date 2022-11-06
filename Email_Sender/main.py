# CODE WITH TOMI -- 20 BEGINNER PYTHON PROJESTS

# Steps
# go over to your email account and setup 2 factor authentication
# generate app password
# create a function to send the email

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'vincentprincewill44@gmail.com'
email_password = 'ukmtfashfpfburfe'

email_reciever = 'vincentprincewill44@yahoo.com'

subject = 'Hey dumb dumb'

body = '''
WHats your putpose
'''

em = EmailMessage()

em['From'] =  email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
