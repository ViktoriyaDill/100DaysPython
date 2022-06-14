from tkinter import *
import pandas as pd
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
timer = ""
new_dict = {}


def get_word():

    global new_dict
    new_dict = choice(data_dict)
    print(new_dict)


def get_english_word():

    global timer
    if timer:
        window.after_cancel(timer)
    get_word()
    canvas.itemconfig(image_container, image=card_front)
    english_word = new_dict["English"]
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(word, text=english_word, fill="black")
    timer = window.after(3000, get_ukrainian_word)


def get_ukrainian_word():

    canvas.itemconfig(image_container, image=card_back)
    ukrainian_word = new_dict["Ukrainian"]
    canvas.itemconfig(title, text="Ukrainian", fill="white")
    canvas.itemconfig(word, text=ukrainian_word, fill="white")


def remove_right():

    global new_dict, data_dict
    data_dict.remove(new_dict)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("./data/learning_word.csv", index=False)
    get_english_word()


window = Tk()
window.title("Study")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Read Flash card
try:
    data = pd.read_csv("./data/learning_word.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/my_word_data.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# Flash Cart
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
image_container = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

card_back = PhotoImage(file="./images/card_back.png")

# Right Button
right = PhotoImage(file="./images/right.png")
button_right = Button(command=remove_right, image=right, highlightthickness=0)
button_right.grid(column=1, row=1)

# Wrong Button
wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(command=get_english_word, image=wrong, highlightthickness=0)
button_wrong.grid(column=0, row=1)

get_english_word()

window.mainloop()