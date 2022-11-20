from turtle import Screen
from player import Player

# to setup the screen/display
screen = Screen()
# to setup the dimensions of the screen
screen.setup(width=600, height=600)
# it dosen't let the screen to show anything
screen.tracer(0)

# using the tuple is important not sure y
player_1 = Player((-100, -280))
player_2 = Player((100, -280))

screen.listen()

screen.onkey(player_1.move_up, "w")
screen.onkey(player_2.move_up, "Up")

# game_is_on = True

while True:
    # updates the screen negating the .tracer()
    screen.update()

# to exit on click
screen.exitonclick()