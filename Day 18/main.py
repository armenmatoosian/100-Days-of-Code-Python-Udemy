# lost my code for challenges 1, 2, and 3 - below is solution code 😒

import turtle as tim
from turtle import Screen
import random

screen = Screen()
# tim = Turtle()
tim.colormode(255)

# my code and solution code mixed
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)
    return random_colours

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.speed(14)
tim.pensize(1)

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

# # my code for challenge 4 - Generate a Random Walk
# heading = [90, 180, 270, 360]
# direction = ["forward", "backward"]
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(heading))
#     tim.fd(20)
#
# # solution code for challenge 4 - Generate a Random Walk
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# my code for challenge 5 - Draw a Spirograph
direction = 0

for _ in range(90):
    tim.color(random_color())
    tim.circle(100)
    direction += 4
    tim.setheading(direction)

# # solution code for challenge 5 - Draw a Spirograph
# tim.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)

screen.exitonclick()