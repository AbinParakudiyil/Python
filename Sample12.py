# Calling function multiple times with different arguments
import turtle
turtle.pensize(4)
turtle.speed(5)
turtle.color("indigo")

'''
Multiple Line Comments

Shape is a function to draw different Polygons
based on number of sides and size of side as its arguments
'''
def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

shape(100,4) #Calling shape function to draw a square
turtle.color("violet")
turtle.penup()
turtle.goto(150,150)
turtle.pendown()
shape(50,6) #Calling shape function to draw a Hexagon
turtle.penup()
turtle.goto(-150, -150)
turtle.color("orange")
turtle.pendown()
shape(150,3) #Calling shape function to draw a triangle

turtle.done()
