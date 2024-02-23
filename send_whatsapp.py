from twilio.rest import Client

# Your Twilio account credentials
account_sid = ACc40d0ee2ffd08a917f479098167ef284
auth_token = 1cb0c73a9c26f6b50f0321c20905417d
from_whatsapp_number = +15169202605
to_whatsapp_number = +917004102260

# Twilio client initialization
client = Client(account_sid, auth_token)

# Send WhatsApp message based on deployment status
status = sys.argv[1]
if status == 'OK':
    message = client.messages.create(
        body="Deployment has been successfully done.",
        from_='whatsapp:' + from_whatsapp_number,
        to='whatsapp:' + to_whatsapp_number
    )
else:
    message = client.messages.create(
        body="Something went wrong! Deployment was unsuccessful.",
        from_='whatsapp:' + from_whatsapp_number,
        to='whatsapp:' + to_whatsapp_number
    )

print(message.sid)
