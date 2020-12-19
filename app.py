from flask import Flask, request

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'

PAGE_ACCESS_TOKEN = "EAA2YfX5EvmQBAAeixF2EDxrGijvj6rZCu6ZABfquFgR2ih84PUAcYdsDvye0WLwPVMsM7C1TrxHLHR4NWYcuWqB6Yv5vJsTnYv3ZBphmg1iE6pDZBRbYZBzJ4dBiVNNaFk0wVSNYOLh7xu7qGHmLwjwtI2ZC5UOgXreDaDEwhuVwZDZD"
VERIFY_TOKEN = "hello"

print("Testtttttt")

def get_bot_response(message):
   
    return "This is a dummy response to ".format(message)


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):

    response = get_bot_response(message)
    send_message(sender, response)


def is_user_message(message):
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


@app.route("/webhook")
def listen():
	print("Hiiiii")
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok"