#import colorgram
import random as rd
import turtle as t
t.colormode(255)
#colors = colorgram.extract('Day 18\daily\hirst.jpg', 12)

rgb_colors=[ (175, 49, 79), (43, 97, 145), (203, 162, 96), (223, 210, 104), (136, 90, 65), (111, 175, 206), 
(176, 164, 40), (211, 132, 173)]

ham=t.Turtle()
ham.shape("turtle")
ham.color('DarkGreen')

def pos(y):
    ham.goto((-200,y-150))

def canvas():
    ham.pendown()
    ham.dot(20, rd.choice(rgb_colors))
    ham.penup()
    ham.forward(50)
    
y=10
ham.penup()
for i in range(10):
    pos(y)
    for j in range(10):
        canvas()
    y += 50

screen = t.Screen()
screen.exitonclick() 