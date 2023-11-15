from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -150
index = 0
for color in colors:
    color = Turtle(shape="turtle")
    color.color(colors[index])
    index += 1
    color.penup()
    color.setpos(-230, y_position)
    y_position += 50
    


screen.exitonclick()