from turtle import Turtle
from random import randint

BALL_MOVE = 10


class Ball(Turtle):

    # create the ball
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_MOVE
        self.y_move = BALL_MOVE

    def starting_direction(self):
        self.setheading(randint(120, 220))

    # make it move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
