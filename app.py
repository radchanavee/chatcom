from flask import Flask, request
import logging


app = Flask("My echo bot")
PAGE_ACCESS_TOKEN = "EAA2YfX5EvmQBAAeixF2EDxrGijvj6rZCu6ZABfquFgR2ih84PUAcYdsDvye0WLwPVMsM7C1TrxHLHR4NWYcuWqB6Yv5vJsTnYv3ZBphmg1iE6pDZBRbYZBzJ4dBiVNNaFk0wVSNYOLh7xu7qGHmLwjwtI2ZC5UOgXreDaDEwhuVwZDZD"
VERIFY_TOKEN = "hello"
print("Testtttttt")


@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"

@app.route('/',methods=['POST'])
def webhook():
	data = request.get_json()
	print("Hi Radchanavee")
	return "ok",200


    

if __name__ == "__main__":
	app.run(port=8000, use_reloader = True)