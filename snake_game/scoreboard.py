from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
         self.goto(0, 0)
         self.write("GAME OVER", align=ALIGN, font=FONT)


    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

