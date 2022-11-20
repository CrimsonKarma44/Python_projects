from turtle import Screen
from player import Player
from cars import CarCreator
from Scoreboard import Board
import time

# to setup the screen/display
screen = Screen()
# to setup the dimensions of the screen
screen.setup(width=600, height=600)
# it dosen't let the screen to show anything
screen.tracer(0)

# using the tuple is important not sure y
player_1 = Player((-100, -280))
player_2 = Player((100, -280))

cars = CarCreator()

scoreboard = Board()

screen.listen()

screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

# another method to reduce the frequency of the cars apperance
# count = 0
while True:
    # Delay in execution of proceeding commands
    time.sleep(0.1)
    # if count%5 == 0:
    cars.create_cars()
    cars.move()

    for car in cars.cars:
        if player_1.distance(car) < 20:
            player_1.restart()
        if player_2.distance(car) < 20:
            player_2.restart()
    
    if player_1.ycor()>230:
        scoreboard.increase1()
        player_1.restart()

    if player_2.ycor()>230:
        scoreboard.increase2()
        player_2.restart()

    # updates the screen negating the .tracer()
    screen.update()
    # count +=1

# to exit on click
screen.exitonclick()