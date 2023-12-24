from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0
        self.r = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r+=1
        self.update()

    def l_point(self):
        self.l+=1
        self.update()