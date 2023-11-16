from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.refresh_scoreboard()
        
    def refresh_scoreboard(self):
        self.setpos(-200, 200)
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=FONT)
        
    def game_over(self):
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT)
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.refresh_scoreboard()
        