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

def draw_circles(amount_of_circles):
    heading = 0
    headingChange = 360 / amount_of_circles
    timmy.speed("fastest")
    for i in range(amount_of_circles):
        timmy.setheading(heading)
        timmy.color(random_color())
        timmy.circle(100)
        heading += headingChange
        
draw_circles(100)

screen = Screen()
screen.exitonclick()
