from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# In a python terminal, run export FLASK_APP="Section54IntroToFlask\420WebServerWithFlask\hello.py"
# Then run python -m flask run