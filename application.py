from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a skeleton Flask App for the WatchTower Application!"
