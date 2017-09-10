import turtle

my_turtle = turtle.Turtle()

my_turtle.speed(10)     # between 0 and 10

for i in range(180):
    my_turtle.forward(100)
    my_turtle.right(30)
    my_turtle.forward(20)
    my_turtle.left(60)
    my_turtle.forward(50)
    my_turtle.right(30)
    my_turtle.penup()
    my_turtle.setposition(0,0)
    my_turtle.pendown()
    my_turtle.right(2)

turtle.done()

