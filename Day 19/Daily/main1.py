#Let's make a Etch-a-Sketch
import turtle as t  

ham = t.Turtle()
ham.color("DarkGreen")
ham.shape("turtle")
screen = t.Screen()

#Let's make the functions that make the turtle move
def mov_forwards():
    ham.forward(20)
def mov_back():
    ham.backward(20)
def clk_wise():
    ham.right(10)
def aclk_wise():
    ham.left(10)
def reset():
    ham.clear()
    ham.penup()
    ham.home()
    ham.pendown()



#Event listeners
screen.listen()
screen.onkey(mov_forwards, "w")
screen.onkey(mov_back, "s")
screen.onkey(aclk_wise, "a")
screen.onkey(clk_wise, "d")
screen.onkey(reset, "c")



screen.exitonclick()