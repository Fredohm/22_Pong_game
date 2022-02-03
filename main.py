# Pong Game
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600

LEFT_PADDLE_STARTING_POS = -350
RIGHT_PADDLE_STARTING_POS = 350

BALL_SPEED = 0.05

# create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# create two paddles
left_paddle = Paddle(LEFT_PADDLE_STARTING_POS)
right_paddle = Paddle(RIGHT_PADDLE_STARTING_POS)

screen.onkeypress(left_paddle.up, "a")
screen.onkeypress(left_paddle.down, "q")

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

# Draw dashed_line in the middle of the screen
net = Turtle("square")
net.color("white")
net.pensize(5)
net.penup()
net.sety(-WIDTH / 2)

while net.ycor() < WIDTH / 2:
    net.pendown()
    net.setheading(90)
    net.forward(40)
    net.penup()
    net.forward(40)

# keep score

ball = Ball()

game_is_on = True
while game_is_on:
    new_ball = False
    ball.setposition(0, 0)
    print("new ball")
    ball.starting_direction()
    while not new_ball:
        screen.update()
        ball.move()
        time.sleep(BALL_SPEED)

        # detect collision with the wall and bounce
        y_pos = ball.ycor()
        x_pos = ball.xcor()
        if y_pos < -290 or y_pos > 290:
            ball.bounce()

        # detect collision with paddle
        if x_pos < 0:
            if left_paddle.distance(ball) < 15:
                ball.setheading(-x_pos)
                break
        else:
            if right_paddle.distance(ball) < 15:
                ball.setheading(x_pos - 180)
                break

        # detect when paddle misses
        if x_pos < -390 or x_pos > 390:
            ball.clear()
            new_ball = True

screen.exitonclick()
