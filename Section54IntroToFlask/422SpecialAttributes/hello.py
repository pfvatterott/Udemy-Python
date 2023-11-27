from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World?</p>"

if __name__ == "__main__":
    app.run()
    # makes it so you can just press the run button. dont have to set the env variable or anything

# In a python terminal, run the following => export FLASK_APP="Section54IntroToFlask\420WebServerWithFlask\hello.py"
# Then run python -m flask run