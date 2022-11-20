from turtle import Turtle, colormode
import random

colormode(255)
class CarCreator():
    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_generator = random.randint(1,5)
        if random_generator == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(281, random.randint(-200,200))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(10)