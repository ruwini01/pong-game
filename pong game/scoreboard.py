from turtle import Turtle, Screen

FONT = ("Courier", 20, "normal")
screen = Screen()
lhs = screen.textinput("Score Board", "Insert LHS Player Name")
rhs = screen.textinput("Score Board", "Insert RHS Player Name")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.goto(100, 250)
        self.write(f"{rhs}: {self.r_score}", align="center", font=FONT)
        self.goto(-100, 250)
        self.write(f"{lhs}: {self.l_score}", align="center", font=FONT)

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_score_board()
        if self.l_score == 15:
            self.goto(0, 0)
            self.write(f"{lhs} is the winner", align="center", font=FONT)

    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.update_score_board()
        if self.r_score == 15:
            self.goto(0, 0)
            self.write(f"{rhs} is the winner", align="center", font=FONT)
