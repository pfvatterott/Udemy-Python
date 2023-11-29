from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World?</p>"

@app.route("/bye")
def bye():
    return 'Bye!'

# @app.route("/username/<name>")
# def greet(name):
#     return f"Hi there {name}"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hi there {name} you are {number} years old!"




if __name__ == "__main__":
    app.run(debug=True) # debugger makes refreshing easy during development









