from turtle import Turtle, Screen
import random



timmy = Turtle()
timmy.shape("turtle")
colors = ["chartreuse", "medium aquamarine", "orange red", "dark magenta", "dark magenta", "gold", "slate gray", "blue violet"]
directions = [0, 90, 180, 270]

timmy.pensize(10) 
timmy.speed("fast")
for i in range(100):
    timmy.color(colors[random.randint(0, len(colors) - 1)])
    timmy.setheading(directions[random.randint(0, len(directions) - 1)])
    timmy.forward(50)
    



screen = Screen()
screen.exitonclick()