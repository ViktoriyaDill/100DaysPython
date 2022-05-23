from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False


color_turtle = []
y = -100
for i in range(6):
    color_turtle.append(Turtle("turtle"))
    color_turtle[i].color(color[i])
    color_turtle[i].penup()
    color_turtle[i].goto(-230, y)
    i += 1
    y += 50


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in color_turtle:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You won. Winner turtle is {winner_turtle}")
            else:
                print(f"You lose. Winner turtle is {winner_turtle}")





screen.exitonclick()
