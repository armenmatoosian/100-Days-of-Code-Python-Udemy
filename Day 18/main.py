# lost my code for parts 1, 2, and 3 - below is solution code 😒

from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

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










for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen.exitonclick()