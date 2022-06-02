from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

# ----------------------random words-----------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=current_card["French"], fill="black")
    canvas.itemconfig(front_canvas, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


# ----------------------Back card-----------------------#

def flip_card():
    canvas.itemconfig(front_canvas, image=card_back_image)
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=current_card["English"], fill="white")


# ----------------------words to learn-----------------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ----------------------UI Setup-----------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
front_canvas = canvas.create_image(400, 263, image=card_front_image)
title_canvas = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
