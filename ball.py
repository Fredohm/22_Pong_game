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

    def starting_direction(self):
        self.setheading(randint(120, 220))

    # make it move
    def move(self):
        self.forward(BALL_MOVE)

    def bounce(self):
        self.setheading(0 - self.heading())
