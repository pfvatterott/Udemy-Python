from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
game_is_on = True

sleep_counter = .05
while game_is_on:
    screen.update()
    time.sleep(sleep_counter)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if (ball.distance(right_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(left_paddle) < 50 and ball.xcor()) < -320:
        ball.bounce_x()
        sleep_counter *= 0.9
        
    if ball.xcor() > 400:
        ball.reset_position()
        sleep_counter = .05
        scoreboard.add_score_left()
        
    
    if ball.xcor() < -400:
        ball.reset_position()
        sleep_counter = .05
        scoreboard.add_score_right()
        

    



screen.exitonclick()
