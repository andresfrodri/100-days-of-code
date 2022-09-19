from snake import Snake
import turtle as t
import time


screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

screen.update()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    

        




screen.exitonclick()