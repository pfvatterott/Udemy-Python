import colorgram
import turtle as t
from turtle import Screen
import random

timmy = t.Turtle()
t.colormode(255)
rgb_colors = []
colors = colorgram.extract(r"Section18GUI\175HirstPainting2\image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
position_x = -200
position_y = -200

def get_random_color():
    return random.choice(rgb_colors)

def set_row():
    for i in range(10):
        timmy.dot(20, get_random_color())
        timmy.forward(50)

for i in range(10):
    timmy.setpos(position_x, position_y)
    set_row()
    position_y += 50
    
screen = Screen()
screen.exitonclick()