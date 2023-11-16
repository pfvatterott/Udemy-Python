import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
car_multiplier = 1
scoreboard = Scoreboard()

loop_index = 6
car_list = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if loop_index % 6 == 0:
        car = CarManager()
        car_list.append(car)
    loop_index += 1
    
    for car in car_list:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()
        car.move_car(car_multiplier) 
       
    if player.ycor() > 290:
        player.reset()
        car_multiplier += .5
        scoreboard.add_score()
        
      




screen.exitonclick()