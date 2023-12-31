from turtle import  Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.speed("fastest")
        segment.penup()
        segment.color("white")
        segment.setposition(position)
        self.segments.append(segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].pos())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setposition(position)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]