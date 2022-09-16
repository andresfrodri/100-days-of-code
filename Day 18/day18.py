from turtle import Turtle, Screen, colormode
import turtle
import random as rd

ham = Turtle()
ham.shape("turtle")
ham.color('DarkGreen')
#Make a square 
for i in range(4):
    ham.forward(100)
    ham.right(90)
ham.left(90)
#Make a dashed line
for i in range(10):
    ham.pencolor('white')
    ham.forward(10)
    ham.pencolor('black')
    ham.forward(10)
ham.left(90)
#Make a dashed line
for i in range(10):
    ham.forward(10)
    ham.penup()
    ham.forward(10)
    ham.pendown()
ham.home()
ham.position()
colormode(255)
def rd_color():
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    v=rd.randint(0,255)
    return r,g,v
#Make figures with different colors 
for i in range(3,5):
    
    ham.pencolor(rd_color())
    for j in range(i):
        ham.color
        ham.right(360/i)
        ham.forward(100)

#Let's make the random walk
ham.clear()

def rand_walk():
    ham.pencolor(rd_color())
    dir=rd.choice([0, 90, 180, 270])
    ham.setheading(dir)
    ham.forward(25)

ham.pensize(15)
ham.speed(10)

for i in range(20):
    rand_walk()

ham.home()
ham.clear()
#Making a spyrograph
ham.speed(0)
ham.pensize(1)
for i in range(0,360,5):
    ham.setheading(i)
    ham.circle(100)
    ham.pencolor(rd_color())


screen = Screen()
screen.exitonclick()  #This has to go at the end of the file