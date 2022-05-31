from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=5, columnspan=2)








window.mainloop()