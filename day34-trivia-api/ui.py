import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"
score = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # BG
        # for creating text, you have to specify the position of the text (150, 125)
        # width on the text is the text wrap
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_canvas = self.canvas.create_text(150, 125, width=280, text="test", fill=THEME_COLOR,
                                                       font=(FONT, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        # don't need self. on button images because it's just going to be used here
        checkmark_img = PhotoImage(file="images/true.png")
        self.checkmark_button = Button(image=checkmark_img, highlightthickness=0, command=self.true_pressed)
        self.checkmark_button.grid(row=2, column=0)

        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        # score label
        self.score_label = Label(text=f"Score: {score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.question_label = Label(text="test", font=(FONT, 20, "italic"))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_canvas, text="You've reached the end of the quiz.")
            self.checkmark_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # self.get_next_question()

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
