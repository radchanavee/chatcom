from flask import Flask, request


app = Flask("My echo bot")

FB_ACCESS_TOKEN = "EAA2YfX5EvmQBAAeixF2EDxrGijvj6rZCu6ZABfquFgR2ih84PUAcYdsDvye0WLwPVMsM7C1TrxHLHR4NWYcuWqB6Yv5vJsTnYv3ZBphmg1iE6pDZBRbYZBzJ4dBiVNNaFk0wVSNYOLh7xu7qGHmLwjwtI2ZC5UOgXreDaDEwhuVwZDZD"


VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200