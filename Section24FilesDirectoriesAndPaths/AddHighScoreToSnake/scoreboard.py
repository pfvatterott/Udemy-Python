from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        self.high_score = 0
        self.refresh_scoreboard()
        
    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} - High Score: {self.high_score}", move=False, align="center", font=('Arial', 20, 'normal'))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_scoreboard()
        
        
    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write(arg=f"GAME OVER", move=False, align="center", font=('Arial', 20, 'normal'))
        
    def add_score(self):
        self.score += 1
        self.refresh_scoreboard()
        
        