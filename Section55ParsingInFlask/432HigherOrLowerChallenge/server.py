from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)



@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZ4OG9ycHQ4emgwaTVqZjNuZGNvZHU3dGx3eXhudHZvMmU5dGd4biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lVN6g7CNgshTtPiG8m/giphy.gif' />"


                  
@app.route("/<guess>") 
def guess(guess):
    if int(guess) > random_number:
        return "<h1>Too high!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    elif int(guess) < random_number:
        return "<h1>Too low!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    else:
        return "<h1>Correct!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    



if __name__ == "__main__":
    app.run(debug=True) # debugger makes refreshing easy during development

# <iframe src="https://giphy.com/embed/lVN6g7CNgshTtPiG8m" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/numeros-novena-lVN6g7CNgshTtPiG8m">via GIPHY</a></p>







