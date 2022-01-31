import turtle

wn = turtle.Screen()
wn.setup(900, 800)
wn.title('animation')
wn.bgcolor('cyan')

N = turtle.Turtle()
N.hideturtle()
N.width(3)
N.color('red', 'yellow' )
N.speed(10)
for i in range(47):
    N.begin_fill()
    N.forward(300)
    N.left(170)
    N.forward(300)
    N.end_fill()
    
turtle.done()