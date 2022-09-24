import turtle as t
import time
from paddle import Paddle   
from ball import Ball

screen = t.Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1= Paddle(-350)
paddle2 = Paddle(350)
screen.update()

ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

game_on = True
x0 = -10
y0 = -10

while game_on:
    paddle2.auto_move()
    screen.update()
   
    if ball.distance(paddle2) < 15:
        x0 = -10
    if ball.distance(paddle1) < 15:
        x0 = 10
    if ball.ycor() > 240:
        y0 = -10
    elif ball.ycor() < -240:
        y0= 10

    ball.goto(ball.xcor() + x0, ball.ycor() + y0)
    time.sleep(0.1)


screen.exitonclick()