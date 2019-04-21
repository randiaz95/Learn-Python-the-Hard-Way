from flask import Flask
from flask import send_from_directory
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
	greeting = "Hello Modafuckas"
	return render_template("index.html", greeting=greeting)

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'favicon'))

if __name__ == "__main__":
	app.run()