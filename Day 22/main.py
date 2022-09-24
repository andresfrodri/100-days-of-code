import turtle as t
import time
from paddle import Paddle   

screen = t.Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1= Paddle(-350)
paddle2 = Paddle(350)
screen.update()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

game_on = True


while game_on:
    paddle2.auto_move()
    screen.update()
    time.sleep(0.1)



screen.exitonclick()