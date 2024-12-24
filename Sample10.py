from turtle import*
from random import randint

speed(0)
colormode(255)
bgcolor("black")

x=1
while x<500:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    color(r,g,b)
    fd(x)
    rt(90.911)

    x=x+1

fd(200)
hideturtle()
done()
