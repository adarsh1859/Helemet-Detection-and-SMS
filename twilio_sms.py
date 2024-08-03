from twilio.rest import Client

from twilio.rest import Client

# Your Twilio account credentials
account_sid = 'lejfbglfskjbn'#enter yout account_sid
auth_token = 'sdlkjgb;ofngeorng'#enter your auth_token

# Create a Twilio client
client = Client(account_sid, auth_token)

# Set the sender's and recipient's phone numbers
sender_number = '+18506417136'
recipient_number = '+919876543210'# enter your phone number

# Your message content
message_body = 'Hello Rider, Kindly waer your helmet while riding the bike'

try:
    # Send the SMS
    message = client.messages.create(
        body=message_body,
        from_=sender_number,
        to=recipient_number
    )
    print("SMS sent successfully!")
    print("Message SID:", message.sid)
except Exception as e:
    print("Error:", e)