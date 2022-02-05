from turtle import Turtle

FONT = ("Courier", 42, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()
        self.draw_net(width=800, height=600)

    # Draw dashed_line in the middle of the screen
    def draw_net(self, width, height):
        self.shape("square")
        self.color("white")
        self.pensize(5)
        self.penup()
        self.goto(0, -height / 2)

        while self.ycor() < width / 2:
            self.pendown()
            self.setheading(90)
            self.forward(40)
            self.penup()
            self.forward(40)

    def update_scoreboard(self):
        self.penup()
        self.goto(-50, 240)
        self.pendown()
        self.write(self.l_score, font=FONT)
        self.penup()
        self.goto(20, 240)
        self.pendown()
        self.write(self.r_score, font=FONT)

    def increase_score(self, x_pos):
        if x_pos < -380:
            self.r_score += 1
        elif x_pos > 380:
            self.l_score += 1
        self.clear()
        self.update_scoreboard()
