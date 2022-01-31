import turtle
import random

turtle.Screen().setup(1500, 800)
N = turtle.Turtle()
N.speed(2)
N.width(10)
N.shape('turtle')
N.turtlesize(2)
N.goto(0,0)
N.hideturtle()
while True:
    x = random.uniform(600, -600)
    y = random.uniform(400, -400)
    N.goto(x,y)

turtle.done()