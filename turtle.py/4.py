import turtle
import math

turtle.screensize(canvwidth=900, canvheight=900)
N = turtle.Turtle()
N.hideturtle()
N.color('red', 'yellow')
N.speed(10)

for i in range(900):
    N.forward(10)
    N.forward(math.sqrt(i))
    N.left(i%180)
    

turtle.done()