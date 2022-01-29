from turtle import Turtle


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
