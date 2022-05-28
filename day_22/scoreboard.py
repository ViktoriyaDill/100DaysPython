from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_side = 0
        self.r_side = 0
        self.update_scoreboard()

    def line(self):
        self.goto(0, -280)
        self.setheading(90)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_scoreboard(self):
        self.line()
        self.goto(-100, 200)
        self.write(self.l_side, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_side, align="center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.clear()
        self.l_side += 1
        self.update_scoreboard()

    def r_score(self):
        self.clear()
        self.r_side += 1
        self.update_scoreboard()