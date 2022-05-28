import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.tracer(0)
FPS = 60 / 1000

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(left_paddle.move_up, "w")

ball = Ball()
score = Scoreboard()

while True:
    time.sleep(FPS)
    screen.update()
    ball.move()
    score.line()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and right_paddle.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and left_paddle.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.missing()
        score.r_score()

    if ball.xcor() < -380:
        ball.missing()
        score.l_score()










screen.exitonclick()