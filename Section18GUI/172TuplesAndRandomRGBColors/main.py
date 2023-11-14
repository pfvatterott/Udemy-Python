import turtle as t
from turtle import Screen
import random


timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(50):
    timmy.color(random_color())

screen = Screen()
screen.exitonclick()