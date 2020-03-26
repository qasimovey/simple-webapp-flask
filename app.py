import os
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route("/info")               # at the end point /info
def getInfo():                    # call method getInfo
    return "Simple Web App!"      # which returns "Simple Web App!"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app