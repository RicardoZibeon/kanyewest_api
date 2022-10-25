import requests
from twilio.rest import Client

account_sid = "AC4aaa90b857921fb02d55c694a5fa1d49"
auth_token = "a1a7b6972c6e44e4990c0a36071cce0f"



response = requests.get("https://api.kanye.rest")
response.raise_for_status()
data = response.json()
quote = data["quote"]

client = Client(account_sid, auth_token)
message = client.messages.create(
    body= f"Hi There , Kanye west quote of the day: {quote}",
    from_="+13608004333",
    to="+27630341790"
)

print(message.status)
