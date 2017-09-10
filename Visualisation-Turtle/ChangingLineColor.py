import turtle

my_turtle = turtle.Turtle()

my_turtle.pencolor('blue')   # hex can also be put into it

for i in range(50):
    my_turtle.forward(50)
    my_turtle.right(123)

my_turtle.pencolor('red')

for i in range(50):
    my_turtle.forward(100)
    my_turtle.left(123)


turtle.done()
