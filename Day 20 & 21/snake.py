import turtle as t

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        X1=0
        for i in range(3):
            segment = t.Turtle(shape="square")
            segment.color('white')
            segment.penup()
            segment.goto(x=X1, y = 0)
            X1 -= 20
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        