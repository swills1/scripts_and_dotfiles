import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

to_emails = [
    ('steven@swills.me')#,
    #('')
]
message = Mail(
    from_email=('alert@swills.me'),
    to_emails=to_emails,
    subject='Coded Message Bravo Zulu Foxtrot',
    html_content='Cool kids ride big wheels. This is an automated emergency test.')
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)