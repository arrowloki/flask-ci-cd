from flask import Flask
from datetime import datetime
app = Flask(__name__)

data = "Hi Loki"

@app.route("/")
def index():
        return "Welcome To My Drinks API"

@app.route('/drinks')
def get_drinks():
    return data


if __name__ == "__main__":
    app.debug = True
    app.run()