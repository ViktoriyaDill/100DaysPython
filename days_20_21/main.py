from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

food = Food()
snake = Snake()
score = Score()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

snake_game_on = True

while snake_game_on:
    screen.update()
    time.sleep(0.1)
    snake.moving_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake_game_on = False
        score.game_over()

    for segment in snake.snake_list:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake_game_on = False
            score.game_over()














screen.exitonclick()