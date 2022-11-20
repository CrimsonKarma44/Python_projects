from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.recreate()

    def recreate(self):
        self.clear()
        self.goto(-210, 250)
        self.write(f" Player 1: {self.player1}", align="center", font=("Courier", 15, "normal"))
        self.goto(200, 250)
        self.write(f" Player 2: {self.player2}", align="center", font=("Courier", 15, "normal"))

    def increase1(self):
        self.player1+=1
        self.recreate()

    def increase2(self):
        self.player2=1
        self.recreate()