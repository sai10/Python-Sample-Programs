import turtle

my_turtle = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

my_turtle.penup()   # so that it does not draws line

for i in range(height):
    for j in range(width):
        my_turtle.dot()
        my_turtle.forward(dot_distance)
    my_turtle.backward(dot_distance*width)
    my_turtle.right(90)
    my_turtle.forward(dot_distance)
    my_turtle.left(90)

turtle.done()
