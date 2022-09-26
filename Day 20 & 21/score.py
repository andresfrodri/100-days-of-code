import turtle as t

class Score(t.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.initial = 0
        self.penup()
        with open('Day 20 & 21\data.txt') as data:
            self.high_score=int(data.read())
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
            with open('Day 20 & 21\data.txt',mode='w') as data:
                f=str(self.high_score)
                data.write(f)

        self.initial = 0
        self.update_scoreboard()
    