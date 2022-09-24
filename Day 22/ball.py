import turtle as t
import random as rd
class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.speed(6)

