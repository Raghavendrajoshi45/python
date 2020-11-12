from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/raghu")
def harry():
    return "Hello harry bhai4!"
app.run(debug=True)
