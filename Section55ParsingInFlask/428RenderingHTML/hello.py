from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style=text-align:center>Hello, World!</h1><p>Paragraph</p>" \
            "<p>paragraph 2</p>" \
            "<img src='https://m.media-amazon.com/images/I/41p6NId+oML._SL1000_.jpg' width=200/>"
                    

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









