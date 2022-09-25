import turtle as t
import time
from paddle import Paddle   
from ball import Ball
from scoreboard import Scoreboard
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
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

#screen.onkey(paddle2.up, "Up")
#screen.onkey(paddle2.down, "Down")

game_on = True

score = Scoreboard()

while game_on:
    #paddle1.auto_move()
    paddle2.auto_move()
    screen.update()
   
    if ball.distance(paddle2) < 50 and ball.xcor()>320 or ball.distance(paddle1) < 50 and ball.xcor()<-320:
        ball.paddler()
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce()
    if ball.xcor() > 380:
        ball.rester()
        score.l_point()
    elif ball.xcor() < -380:
        ball.rester()
        score.r_point()

    ball.move()
 
    time.sleep(0.041)


screen.exitonclick()