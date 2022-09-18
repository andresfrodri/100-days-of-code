import turtle as t  

ham = t.Turtle()
ham.color("DarkGreen")
ham.shape("turtle")
screen = t.Screen()

def mov_forwards():
    ham.forward(20)

screen.listen()
screen.onkey(mov_forwards, "space")

screen.exitonclick()