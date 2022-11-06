from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'vincentprincewill44@gmail.com'
email_password = 'ukmtfashfpfburfe'

i = ['vincentprincewill44@yahoo.com', 'princewill.m1801343@st.futminna.edu.ng']

subject = 'Hey dumb dumb'

body = '''
WHats your putpose
'''



for email_reciever in i:
    em = EmailMessage()
    em['From'] =  email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

