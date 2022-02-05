# Pong Game
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

LEFT_PADDLE_STARTING_POS = -350
RIGHT_PADDLE_STARTING_POS = 350

BALL_SPEED = 0.1

# create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# create two paddles
l_paddle = Paddle(LEFT_PADDLE_STARTING_POS)
r_paddle = Paddle(RIGHT_PADDLE_STARTING_POS)

screen.onkeypress(l_paddle.up, "a")
screen.onkeypress(l_paddle.down, "q")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

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

# create scoreboard
scoreboard = Scoreboard()

ball = Ball()

game_is_on = True
while game_is_on:
    new_ball = False
    ball.setposition(0, 0)

    while not new_ball:
        screen.update()
        ball.move()
        time.sleep(BALL_SPEED)

        # detect collision with the wall and bounce
        y_pos = ball.ycor()
        x_pos = ball.xcor()
        if y_pos < -290 or y_pos > 290:
            ball.bounce_y()

        # detect collision with paddle
        if ball.distance(l_paddle) < 50 and ball.xcor() < -330 or ball.distance(r_paddle) < 50 and ball.xcor() > 330:
            ball.bounce_x()

        # detect when paddle misses
        if x_pos > 390:
            ball.reset_position()
            scoreboard.increase_score(x_pos)
            scoreboard.update_scoreboard()
            new_ball = True

        if ball.xcor() < -390:
            ball.reset_position()
            scoreboard.increase_score(x_pos)
            scoreboard.update_scoreboard()
            new_ball = True

screen.exitonclick()
