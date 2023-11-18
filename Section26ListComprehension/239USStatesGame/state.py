from turtle import Turtle
FONT = ("Courier", 10, "normal")

class State(Turtle):
    def __init__(self, x_value, y_value, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x_value, y_value)
        self.write(arg=state_name, move=False, align="center", font=FONT)
    
