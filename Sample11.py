import turtle

turtle.pensize(4)
turtle.speed(5)
turtle.color("indigo")

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

shape(100,4) # Calling function with values of size and sides
turtle.done()
