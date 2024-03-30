from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.update_scoreboard()
    def update_scoreboard(self):

        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()

    def increase_bonus(self):

        self.score += 5
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        gameover = self.clone()
        gameover.goto(0,0)
        gameover.write(arg=" GAME OVER !!!", align=ALIGNMENT, font= ("Arial",25,"normal"))