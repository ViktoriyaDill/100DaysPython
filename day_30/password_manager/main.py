import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_l = [random.choice(letters) for l in range(nr_letters)]
    password_s = [random.choice(symbols) for l in range(nr_symbols)]
    password_n = [random.choice(numbers) for l in range(nr_numbers)]
    password_list = password_n + password_l + password_s

    random.shuffle(password_list)
    password_input.insert(0, ''.join(password_list))

    pyperclip.copy(''.join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_string = web_input.get().lower()
    email_string = email_input.get()
    password_string = password_input.get()

    if web_string == "" or password_string == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
        return None

    ask_window = messagebox.askokcancel(title=web_string, message=f"There are the details entered:\n"
                                                                  f"Email: {email_string}\n"
                                                                  f"Password: {password_string}\nIs it ok to save?")
    new_dict = {web_string: {
        "Email": email_string,
        "Password": password_string,
    }}

    if ask_window:
        try:
            with open("Data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Data.json", mode="w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            data.update(new_dict)
            with open("Data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


def search():
    web_string = web_input.get().lower()
    try:
        with open("Data.json", "r") as data_file:
            data_dict = json.load(data_file)
        result = data_dict[web_string]
    except KeyError:
        messagebox.showerror(title="Oops", message="No details for the website!")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found!")
    else:
        messagebox.showinfo(title=f"{web_string}", message=f"Email: {result['Email']}\nPassword: {result['Password']}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:", bg=WHITE)
website.grid(column=0, row=1)

user_name = Label(text="Email/Username:", bg=WHITE)
user_name.grid(column=0, row=2)

password = Label(text="Password:", bg=WHITE)
password.grid(column=0, row=3)

# Entry
web_input = Entry(width=21, highlightthickness=0)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = Entry(width=35, highlightthickness=0)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "viktoriadill@google.com")
password_input = Entry(highlightthickness=0, width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate", bg=WHITE, highlightthickness=0, width=10, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, bg=WHITE, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", bg=WHITE, highlightthickness=0, width=10, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
