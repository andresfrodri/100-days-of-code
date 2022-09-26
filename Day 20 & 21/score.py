import turtle as t

class Score(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.initial = 0
        self.penup()
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=20, y= 280)
        self.clear()
        self.write(f'Score: {self.initial} High Score : { self.high_score}' , align= 'center', font=('consolas', 12, 'normal'))
    #def game_over(self):
    #    self.goto(0,0)
    #    self.write('GAME OVER',move = False, align= 'center', font=('consolas', 14, 'normal'))
    
    def reset(self):
        if self.initial > self.high_score:
            self.high_score = self.initial
        self.initial = 0
        self.update_scoreboard()
    