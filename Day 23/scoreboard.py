from turtle import Turtle, update

FONT = ("Courier", 22, "normal")    

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f'level: {self.score}', align='center', font=FONT)

    def point(self):
        self.score += 1
        self.update()

    def dead(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
