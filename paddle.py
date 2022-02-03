from turtle import Turtle

SPEED_MOVE = 20

NORTH = 90
SOUTH = 270


class Paddle(Turtle):

    def __init__(self, x):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def up(self):
        new_y = self.ycor() + SPEED_MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - SPEED_MOVE
        self.goto(self.xcor(), new_y)
