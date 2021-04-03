from flask import Flask


app = Flask(__name__)
@app.route("/")
def index():
	print("test")
	return "Hello"
app.run(debug = True, host = "192.168.55.78", port = 80)