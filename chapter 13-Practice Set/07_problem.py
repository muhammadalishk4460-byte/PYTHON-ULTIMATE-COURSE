from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>rehan is a bad boy</p>"
app.run()