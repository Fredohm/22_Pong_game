# Pong Game
from turtle import Turtle, Screen
from paddle import Paddle

WIDTH = 800
HEIGHT = 600

LEFT_PADDLE_STARTING_POS = [(-360, -20), (-360, 0), (-360, 20)]
RIGHT_PADDLE_STARTING_POS = [(360, -20), (360, 0), (360, 20)]

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
screen.update()

# create the ball and make it move

# detect collision with the wall and bounce

# detect collision with paddle

# detect when paddle misses

# keep score

screen.exitonclick()
