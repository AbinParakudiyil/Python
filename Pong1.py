#PONG V1
#GAME WINDOW/SCREEN

import turtle as t
import random
import winsound

wn=t.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score

score_a=0
score_b=0


#PADDLE A

paddle_a=t.Turtle()
paddle_a.speed(0)
paddle_a.color("purple")
paddle_a.shape("square") #Default Size 20*20 Pixels
paddle_a.shapesize(stretch_wid=5,stretch_len=1)# Now 100*20
paddle_a.penup()
paddle_a.goto(-350,0)

#PADDLE B

paddle_b=t.Turtle()
paddle_b.speed(0)
paddle_b.color("purple")
paddle_b.shape("square") #Default Size 20*20 Pixels
paddle_b.shapesize(stretch_wid=5,stretch_len=1)# Now 100*20
paddle_b.penup()
paddle_b.goto(350,0)

#BALL

ball=t.Turtle()
ball.speed(5)
ball.color("yellow")
ball.shape("circle")
ball.penup()
ball.goto(0,0)

ball.dx=1
ball.dy=1

#PEN

pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B:0",align="center",font=("Courier",24,"normal"))
#FUNCTIONS

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    if y>=250:
        y=250 #stops at boundaries
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    if y<=-250:
        y=-250 #stops at boundaries
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    if y>=250:
        y=250 #stops at boundaries
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    if y<=-250:
        y=-250 #stops at boundaries
    paddle_b.sety(y)

#KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
    
#MAIN GAME LOOP

while True:
    wn.update()

    #MOVE THE BALL

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #BORDER CHECK

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        #os.system("aplay bounce.wav&") for Linux
        #os.system("afplay bounce.wav&") for Mac
        #SND_ASYNC or & use for sync hit and sound
        #ball.dy *=random.choice([-1,1])

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        #ball.dy *=random.choice([-1,1])

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))


    #if ball.xcor()>390:
        #ball.goto(0,0)
        #ball.dx *=random.choice([-1,1])

    #if ball.xcor() < -390:
        #ball.goto(0,0)
        #ball.dx *= random.choice([-1,1])

    #PADDLE AND BALL COLLISSIONS

    if (ball.xcor()>330 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50) and (ball.ycor()>paddle_b.ycor()-50):
         ball.setx(330)  # Correct x-coordinate for the right paddle
         ball.dx *= -1
         winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if (ball.xcor()<-330 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50) and (ball.ycor()>paddle_a.ycor()-50):
         ball.setx(-330)  # Correct x-coordinate for the left paddle
         ball.dx *= -1
         winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    
