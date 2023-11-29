from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        html = function()
        return f"<b>{html}</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        html = function()
        return f"<em>{html}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        html = function()
        return f"<u>{html}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "<h1 style=text-align:center>Hello, World!</h1><p>Paragraph</p>" \
            "<p>paragraph 2</p>" \
            "<img src='https://m.media-amazon.com/images/I/41p6NId+oML._SL1000_.jpg' width=200/>"
                    

@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hi there {name} you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True) # debugger makes refreshing easy during development









