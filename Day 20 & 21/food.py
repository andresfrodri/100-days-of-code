import turtle as t
import random as rd
class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color('red')
        self.speed(0)
        self.refresh()
    
    def refresh(self):
        random_x = rd.randint(-280,280)
        random_y = rd.randint(-280,280)
        self.goto(random_x, random_y)
