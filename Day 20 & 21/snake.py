import turtle as t


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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
        self.head.forward(20)
        
    def up(self):
        if self.head.heading() != 270:
           self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def reset(self):
        for seg in  self.segments:
            seg.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def new_segment(self):
        segment = t.Turtle(shape="square")
        segment.color('white')
        segment.penup()
        self.segments.append(segment)
        
        