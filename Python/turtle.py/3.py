import turtle
import math

turtle.screensize(canvwidth=900, canvheight=900)
N = turtle.Turtle()
N.hideturtle()
N.color('red', 'yellow')
N.speed(10)
N.width(1.5)
for i in range(2000):
    N.forward(10)
    N.left(math.sin(i/10)*25)
    N.left(20)
    

turtle.done()