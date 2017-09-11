import turtle

my_turtle = turtle.Turtle()

numSides = 6
sideLength = 70
angle = 360.0/numSides

for i in range(numSides):
    my_turtle.forward(sideLength)
    my_turtle.right(angle)

turtle.done()
