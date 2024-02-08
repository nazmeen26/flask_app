rom flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"


@app.route("/")
def welcome_corporation():
    return ("Company Name: ABC Corporation <br>"
        "Location: India <br>"
        "Contact Detail: 999-999-9999")

if __name__=="__main__":
    app.run(host="0.0.0.0")
