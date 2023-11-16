from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.refresh_scoreboard()
        
    def refresh_scoreboard(self):
        self.setpos(-100, 200)
        self.write(arg=self.left_score, move=False, align="center", font=('Arial', 20, 'normal'))
        self.setpos(100, 200)
        self.write(arg=self.right_score, move=False, align="center", font=('Arial', 20, 'normal'))
        
    def game_over(self):
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=('Arial', 20, 'normal'))
        
    def add_score_left(self):
        self.clear()
        self.left_score += 1
        self.refresh_scoreboard()
        
    def add_score_right(self):
        self.clear()
        self.right_score += 1
        self.refresh_scoreboard()
        
    
        
        