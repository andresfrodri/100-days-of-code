import turtle as t


class paddle(t.Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.x = x
        self.create_paddle()



    def create_paddle(self):
        segment = t.Turtle(shape="square")
        segment.setheading(90)
        segment.shapesize(stretch_wid=5, stretch_len=1)
        segment.color('white')
        segment.penup()
        segment.goto(self.x, y = 0)

    def up(self):
        self.setheading(90)
        self.forward(20)


    def down(self):
        self.setheading(270)
        self.forward(20)

    def move(self):
        self.forward(20)

    def auto_move(self):
        if self.center.ycor() == 240:
            self.down()
        elif self.center.ycor() == -240:
            self.up()
        else:
            self.move()



