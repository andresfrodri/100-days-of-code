from msilib.schema import Class
import turtle as t
from venv import create


class paddle(t.Turtle):
    def __init__(self, x):
        super().__init__()
        self.segments = []
        self.shape('square')
        self.x = x
        self.create_paddle()
        self.center = self.segments[2]


    def create_paddle(self):
        y1 = 40
        for segment in range(5):
            segment = t.Turtle(shape="square")
            segment.setheading(90)
            segment.speed(0)
            segment.color('white')
            segment.penup()
            segment.goto(self.x, y = y1)
            y1 -= 20
            self.segments.append(segment)
    
    def up(self):
        for i in self.segments:
            i.setheading(90)
            i.speed(0)
            i.forward(20)

    def down(self):
        for i in self.segments:
            i.setheading(270)
            i.forward(20)
    def move(self):
        for i in self.segments:
            i.forward(20)

    def auto_move(self):

        if self.center.ycor() == 240:
            self.down()
        elif self.center.ycor() == -240:
            self.up()
        else:
            self.move()



