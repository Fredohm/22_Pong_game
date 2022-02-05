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
