from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

converted_ans = Label(text="")
converted_ans.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)


def button_clicked():
    user_input = int(input.get())
    converted = round(user_input * 1.6, 2)
    converted_ans.config(text=converted)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
