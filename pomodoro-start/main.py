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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_func():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


timer_label = Label(text="Timer", bg=PINK, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=3)

checkmarks = Label(text="✔", bg=PINK, fg=GREEN, font=(FONT_NAME, 12, "bold"))
checkmarks.grid(column=2, row=3)

window.mainloop()


