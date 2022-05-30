import turtle
import pandas

screen = turtle.Screen()
screen.title("USA states game")
images = "blank_states_img.gif"
screen.addshape(images)
screen.bgpic(images)
turtle.penup()
turtle.hideturtle()

data_states = pandas.read_csv("50_states.csv")
data_states_list = data_states["state"].to_dict()
x_pos = data_states["x"].to_dict()
y_pos = data_states["y"].to_dict()

guess_state = []
score = 0
is_exit = False
while score < 50:
    answer_state = screen.textinput(title=f"Score: {score}/{len(data_states_list)} States correct",
                                    prompt="What's another state name?").title()
    for key in data_states_list:
        if answer_state == "Exit":
            not_used_state = data_states[~data_states["state"].isin(guess_state)]
            not_used_state.to_csv("not_used_state.csv")
            is_exit = True
            break
        if data_states_list[key] == answer_state:
            turtle.goto(x_pos[key], y_pos[key])
            turtle.write(data_states_list[key], align="center", font=("Arial", 8, 'normal'))
            guess_state.append(data_states_list[key])
            score += 1
    if is_exit:
        break

