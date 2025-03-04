import turtle

screen = turtle.Screen()
screen.screensize(1000, 500)
screen.bgcolor('white')

t = turtle.Turtle()
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.goto(-70, -4)


turtle.done()