import turtle
import time
import winsound

wn  = turtle.Screen()
wn.title("Pong by @nup")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(385,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font = ("courier", 24, "normal"))
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") 
wn.onkeypress(paddle_a_down,"s") 
wn.onkeypress(paddle_b_up,"Up") 
wn.onkeypress(paddle_b_down,"Down")
# main loop
while True:
    wn.update()
    time.sleep(1/100000)
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 399:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font = ("courier", 24, "normal"))


    if ball.xcor() < -399:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font = ("courier", 24, "normal"))

    # collision
    if ball.xcor() > 360 and ball.ycor() < (paddle_b.ycor() +40) and ball.ycor() > (paddle_b.ycor() -40):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -360 and ball.ycor() < (paddle_a.ycor() +40) and ball.ycor() > (paddle_a.ycor() -40):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)