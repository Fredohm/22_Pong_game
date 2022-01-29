from turtle import Turtle
from random import randint


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
        self.forward(100)
