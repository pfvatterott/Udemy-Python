from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
   def __init__(self):
      super().__init__()
      self.penup()
      self.shape("turtle")
      self.setheading(90)
      self.setposition(0, -280)
   
   def up(self):
      self.forward(MOVE_DISTANCE)

   def reset(self):
      self.setposition(0, -280)