from tracemalloc import start
import turtle as t
import time


screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

x1=0
segments = []
for i in range(3):
    segment = t.Turtle(shape="square")
    segment.color('white')
    segment.penup()
    segment.goto(x=x1, y = 0)
    x1 -= 20
    segments.append(segment)

screen.update()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

        




screen.exitonclick()