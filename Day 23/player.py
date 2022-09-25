from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = STARTING_POSITION 
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.begin_level()
    def move(self):
        self.goto(self.xcor(),self.ycor()+ MOVE_DISTANCE)

    def begin_level(self):
        self.goto(self.STARTING_POSITION)
    