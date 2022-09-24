import turtle as t


class Paddle(t.Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.x = x
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color('white')
        self.penup()
        self.goto(self.x, 0)


        
    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)

    def move(self):
        if self.heading() == 90:
            self.goto(self.xcor(),self.ycor()+20)
        else:
            self.goto(self.xcor(),self.ycor()-20)
    

    def auto_move(self):

        if self.ycor() > 220:
            self.down()
            self.setheading(270)
        elif self.ycor() < -220:
            self.up()
            self.setheading(90)
        else:
            self.move()
        





