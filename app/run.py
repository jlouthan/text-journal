from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	response = twilio.twiml.Response()
	response.message('Hello...')
	return str(response)

@app.route('/hello', methods=['GET'])
def hello_jenny():
	return 'hello jenny'

if __name__ == '__main__':
	app.run(debug=True)