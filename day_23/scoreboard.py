from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1

    def change_level(self, player):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        if player.ycor() > 280:
            self.level += 1
            return True

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

