from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")
miles = Label(text="Miles", font=("Arial", 16, "italic"))
miles.grid(column=2, row=0)
text = Label(text="is equal to ", font=("Arial", 16, "italic"))
text.grid(column=0, row=1)
equal = Label(text="0", font=("Arial", 16, "italic"))
equal.grid(column=1, row=1)
km = Label(text="Km", font=("Arial", 16, "italic"))
km.grid(column=2, row=1)


def button_click():
    equal["text"] = round(1.6 * float(input.get()), 2)


my_button = Button(text="Calculate", font=("Helvetica", 12, "normal"), command=button_click)
my_button.grid(column=1, row=2)

input = Entry(width=10)
input.insert(END, "0")
input.grid(column=1, row=0)

window.mainloop()

