# lost my code for challenges 1, 2, and 3 - below is solution code 😒

from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.speed(7)
tim.pensize(10)

# # solution code specific to challenge 3 - Drawing Different Shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# my code for challenge 4 - Generate a Random Walk
heading = [90, 180, 270, 360]
direction = ["forward", "backward"]
for _ in range(100):
    tim.color(random.choice(colours))
    tim.setheading(random.choice(heading))
    tim.fd(20)

# solution code for challenge 4 - Generate a Random Walk
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))










screen.exitonclick()