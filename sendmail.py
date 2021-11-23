import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "steven@swills.me"
        }
      ],
      "subject": "Coded Message Bravo Zulu Foxtrot"
    }
  ],
  "from": {
    "email": "steven@swills.me"#,
    #"name": "Manny"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "Cool kids ride a big wheel. This is a test of the emergency broadcast system."
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)