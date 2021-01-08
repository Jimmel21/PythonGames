
import turtle
import winsound

window = turtle.Screen()
window.title("Pong: Classic")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white") 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #do not draw line while moving 
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #do not draw line while moving 
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white") 
ball.penup() #do not draw line while moving 
ball.goto(0, 0)
balldx = 0.21
balldy = -0.21

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

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

#Keyboard binding
# when the user presses a button, call the respective function to move the object
window.listen()
window.onkeypress(paddle_a_up, "w") 
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()
    
    #Move the ball
    ball.setx(ball.xcor() + balldx)
    ball.sety(ball.ycor() + balldy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        balldy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        balldy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        balldx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        balldx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    
    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        balldx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        balldx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    