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
        self.penup()
        self.color('white')
        self.goto(-500,-500)
        self.creator()
        
    
    def creator(self):
        random_chance = rd.randint(1, 3)
        if random_chance == 1:
            car = Turtle('turtle')
            car.setheading(180)
            car.shapesize(stretch_len=3.5, stretch_wid=1.3)
            car.shape('square')
            car.color(rd.choice(COLORS))
            car.penup()
            car.goto(280, rd.randint(-250,250))
            self.car_set.append(car)


    def move(self):
        for car in self.car_set:
            car.forward(self.STARTING_MOVE_DISTANCE)
    
    def next_level(self):
        self.STARTING_MOVE_DISTANCE += 10