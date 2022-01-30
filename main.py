# Pong Game
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600

LEFT_PADDLE_STARTING_POS = [(-360, -20), (-360, 0), (-360, 20)]
RIGHT_PADDLE_STARTING_POS = [(360, -20), (360, 0), (360, 20)]

GAME_SPEED = 0.1

# create screen
screen = Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Draw dashed_line in the middle of the screen
net = Turtle("square")
net.color("white")
net.pensize(10)
net.penup()
net.sety(-WIDTH / 2)

while net.ycor() < WIDTH / 2:
    net.pendown()
    net.setheading(90)
    net.forward(40)
    net.penup()
    net.forward(40)


# create two paddles
left_paddle = Paddle()
left_paddle.create_paddle(LEFT_PADDLE_STARTING_POS)

right_paddle = Paddle()
right_paddle.create_paddle(RIGHT_PADDLE_STARTING_POS)


# detect collision with paddle

# detect when paddle misses

# keep score

ball = Ball()

game_is_on = True
while game_is_on:
    new_ball = False
    ball.setposition(0, 0)
    ball.starting_direction()
    while not new_ball:
        screen.update()
        ball.move()
        time.sleep(GAME_SPEED)

        # detect collision with the wall and bounce
        y_pos = ball.ycor()
        x_pos = ball.xcor()
        if y_pos < -290 or y_pos > 290:
            print(f"y: {y_pos}")
            ball.bounce()
            pass

        if x_pos < -390 or x_pos > 390:
            print(f"x: {x_pos}")
            new_ball = True

screen.exitonclick()
