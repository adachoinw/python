from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#pack() puts it in the centre of the screen
my_label.grid(column=0, row=0)

#button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

new_button = Button(text="click me")
new_button.grid(column=2, row=0)



window.mainloop()