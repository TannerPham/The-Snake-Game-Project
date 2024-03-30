from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()

    def draw_border(self):
        self.teleport(-290, -290)
        for _ in range(4):
            self.pencolor("white")
            self.forward(580)
            self.setheading(90+ _*90)
            self.hideturtle()
