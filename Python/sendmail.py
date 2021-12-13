import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

to_emails = [
    ('email@email.com')#,
    #('')
]
message = Mail(
    from_email=('email@email.com'),
    to_emails=to_emails,
    subject='Email Subject',
    html_content='Cool kids ride big wheels.')
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)