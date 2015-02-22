from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

thing_list = ['one thing', 'a second thing']

@app.route("/", methods=['GET'])
def show_things():
	return str(thing_list)

@app.route('/', methods=['POST'])
def receive_text():
	response = twilio.twiml.Response()
	new_thing = request.values.get('Body', None)
	print new_thing
	thing_list.append(new_thing)
	response.message('Thing received: ' + new_thing)
	return str(response)

@app.route('/hello', methods=['GET'])
def hello_jenny():
	return 'hello jenny'

if __name__ == '__main__':
	app.run(debug=True)
