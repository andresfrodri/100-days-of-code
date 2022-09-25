import turtle as t
import random as rd
class Ball(t.Turtle):

    def __init__(self):
        l0=[10,-10]
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.speed(6)
        self.x_move = rd.choice(l0)
        self.y_move = rd.choice(l0)
    
    def move(self):
        new_x = self.xcor() +  self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce(self):
        self.y_move = -self.y_move
    def paddler(self):
        self.x_move = (-1.1)*self.x_move
    
    def rester(self):
        l0=[10,-10]
        self.paddler()
        if self.x_move > 0:
            self.x_move =10
        else:
            self.x_move = -10
        self.y_move = rd.choice(l0)
        self.home()



