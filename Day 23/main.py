import time
import random as rd
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
ham = Player()
screen.listen()
screen.onkey(ham.move, "w")
car= CarManager()
scorer = Scoreboard()

game_is_on = True

while game_is_on:
    car.move()
    time.sleep(0.1)
    screen.update()
    if ham.ycor() >= 280:
        ham.begin_level()
        car.next_level()
        scorer.point()
    if car.xcor() <= -280:
        car.begin_level()

screen.exitonclick()