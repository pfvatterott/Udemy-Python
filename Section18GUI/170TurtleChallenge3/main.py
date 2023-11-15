from turtle import Turtle, Screen
import random



timmy = Turtle()
timmy.shape("turtle")
colors = ["chartreuse", "medium aquamarine", "orange red", "dark magenta", "dark magenta", "gold", "slate gray", "blue violet"]

def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 10):
    timmy.color(colors[random.randint(0, len(colors) - 1)])
    draw_shape(i)
    



screen = Screen()
screen.exitonclick()