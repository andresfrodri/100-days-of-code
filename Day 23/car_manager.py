from turtle import Turtle
import random as rd
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_set=[]
        self.STARTING_MOVE_DISTANCE = 5
        self.creator()
    
    def creator(self):
        self.setheading(180)
        self.shapesize(stretch_len=3.5, stretch_wid=1.3)
        self.shape('square')
        self.color(rd.choice(COLORS))
        self.penup()
        self.begin_level()

    def begin_level(self):
        self.goto(280, rd.randint(-250,250))

    def move(self):
        self.forward(self.STARTING_MOVE_DISTANCE)
    
    def next_level(self):
        self.STARTING_MOVE_DISTANCE += 10
