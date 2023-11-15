from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        self.refresh_scoreboard()
        
    def refresh_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))
        
    def game_over(self):
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=('Arial', 20, 'normal'))
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.refresh_scoreboard()
        
        