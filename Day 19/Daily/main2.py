import turtle as t  
import random as rd


screen = t.Screen()

screen.setup(width=500, height=500)
race_on = False
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

y1 = 162.34
colors =  ['red','orange', 'yellow', 'green', 'blue', 'purple']
turtles=[]
for i in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-220, y = y1)
    y1 -= 66.66 
    turtles.append(new_turtle)
if bet:
    race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")                
        random_distance=rd.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()