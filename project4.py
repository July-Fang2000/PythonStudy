from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC46eb7c940ce1208855786706a9dfd7cb"
# Your Auth Token from twilio.com/console
auth_token  = "5d3afc01b5b17329e5605a145b5eb230"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19515482691",
    from_="+19707071071",
    body="Dear son")

print(message.sid)