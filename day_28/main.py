from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
coef = 1
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button_click():

    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    text.config(text="Timer", fg=GREEN)
    mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_click():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        text.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        text.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        text.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    min, sec = divmod(count, 60)
    global coef, timer
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(time_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button_click()
        if reps % 2 == 0:
            mark.config(text="✔" * coef)
            coef += 1

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

text = Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
text.grid(column=1, row=0)
mark = Label(font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
mark.grid(column=1, row=4)


start_button = Button(text="Start", font=("Helvetica", 12, "normal"), command=start_button_click, highlightthickness=0)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", font=("Helvetica", 12, "normal"), command=reset_button_click, highlightthickness=0)
reset_button.grid(column=2, row=3)

window.mainloop()