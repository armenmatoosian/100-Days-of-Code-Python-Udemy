import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COORDINATE = random.randint(-250, 250)
all_cars = []

# #my code for Create the Car Behaviour
# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.shape("square")
#         self.shapesize(1, 2)
#         self.seth(180)
#         self.new_car = ()
#
#     # my code for Create the Car Behaviour
#     def new(self):
#         self.color(random.choice(COLORS))
#         self.setpos(350, Y_COORDINATE)
#
#     # my code for Create the Car Behaviour
#     def move(self):
#         new_x = self.xcor() - STARTING_MOVE_DISTANCE
#         new_y = 0
#         self.goto(new_x, new_y)
#
#     # my code for Create the Car Behaviour
#     def increase_speed(self):
#         self.goto(0, 0)

# solution code for Create the Car Behaviour
class CarManager():

    def __init__(self):
        self.all_cars = [] #this is what I was missing from my code
        self.car_speed = STARTING_MOVE_DISTANCE # my code Detect when the PLayer has reached the other side

    def create_car(self):
        random_chance = random.randint(1, 6) #I was close to getting this, there was no need to count to or from 6
        if random_chance == 1:
            new_car = Turtle("square") #this is what I was missing from my code
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) #this is where the append to list should be

    def move_cars(self):
        for car in self.all_cars: #this is where and how the for loop should be, referencing list of cars created above
            car.backward(self.car_speed)

    # my code Detect when the PLayer has reached the other side
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT