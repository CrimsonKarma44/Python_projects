from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        # i believe this imports shape and can also be given a fiel in directory
        self.shape("turtle")
        # 90a as in degree it's default is 0
        self.setheading(90)
        # the .penup() is to stop itfrom drawing a line as it mmoves
        self.penup()
        # to move its position
        self.goto(position)
        self.color("blue")
    def move_up(self):
        # to move it along the y axis
        self.forward(10)