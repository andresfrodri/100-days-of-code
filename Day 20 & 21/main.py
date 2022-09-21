from snake import Snake
from food import Food
from score import Score 
import turtle as t
import time


screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_title = Score()

score_title.goto(x=-20, y= 280)
score_title.write('score: ',move = False, align= 'center', font=('consolas', 14, 'normal'))
score = Score()
score.goto(x=20, y= 280)
initial = 0
score.write(initial ,move = False, align= 'center', font=('consolas', 14, 'normal'))
screen.update()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        initial += 1
        score.write(initial ,move = False, align= 'center', font=('consolas', 12, 'normal'))
        snake.new_segment()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False #This freezes the game
        game_over = Score()
        game_over.write('GAME OVER',move = False, align= 'center', font=('consolas', 14, 'normal'))




        




screen.exitonclick()