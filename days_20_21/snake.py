from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        self.snake_list.append(snake)
        snake.goto(position)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def moving_snake(self):
        for pos in range(len(self.snake_list) - 1, 0, -1):
            pos_x = self.snake_list[pos - 1].xcor()
            pos_y = self.snake_list[pos - 1].ycor()
            self.snake_list[pos].goto(pos_x, pos_y)
        self.snake_list[0].forward(MOVING)

    def move_up(self):
        start_position = self.snake_list[0].heading()
        if start_position == 0 or start_position == 180:
            self.snake_list[0].setheading(90)

    def move_down(self):
        start_position = self.snake_list[0].heading()
        if start_position == 0 or start_position == 180:
            self.snake_list[0].setheading(270)

    def move_left(self):
        start_position = self.snake_list[0].heading()
        if start_position == 90 or start_position == 270:
            self.snake_list[0].setheading(180)

    def move_right(self):
        start_position = self.snake_list[0].heading()
        if start_position == 90 or start_position == 270:
            self.snake_list[0].setheading(0)

