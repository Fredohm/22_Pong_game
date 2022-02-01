from turtle import Turtle

SPEED_MOVE = 20

NORTH = 90
SOUTH = 270


class Paddle:

    def __init__(self):
        self.segments = []
        self.create_paddle([])

    def create_paddle(self, positions):
        for position in positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        for segment in self.segments:
            segment.setheading(NORTH)
            segment.forward(SPEED_MOVE)

    def down(self):
        for segment in self.segments:
            segment.setheading(SOUTH)
            segment.forward(SPEED_MOVE)

