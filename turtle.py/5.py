import turtle

N = turtle.Turtle()

N.getscreen().bgcolor('#ffab2e')

N.penup()
N.goto((-200, 100))
N.pendown()
N.hideturtle()
N.speed(10)
N.width(1.5)

def star(N, size):
    if size<10:
        return 
    else:
        N.begin_fill()
        for i in range(5):
            N.forward(size)
            star(N, size/3)
            N.left(216)
    N.end_fill()
star(N, 360)

turtle.done()