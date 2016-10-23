import sendgrid
import os
from sendgrid.helpers.mail import *

def sendMail(sender, receiver, subject, message):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(sender)
    to_email = Email(receiver)
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
