from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.paddles = []
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len= 5, stretch_wid=1)
        self.setheading(90)
        
    def up(self):
        self.setheading(90)
        self.forward(40)
        
    def down(self):
        self.setheading(270)
        self.forward(40)