# import colorgram
# from main import screen
import random

# #my code for Hirst Painting project part 1
# colours_from_image = (colorgram.extract('image.jpg', 30))
# colour_list = []
#
# for colour_number in range(30):
#     current_colour = colours_from_image[colour_number]
#     rgb = (current_colour.rgb[0], current_colour.rgb[1], current_colour.rgb[2])
#     colour_list.append(rgb)
#
# print(colour_list)
#
# #solution code for Hirst Painting project part 1
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

colour_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as tim
from turtle import Screen

#my code for Hirst Painting project part 2, forgot to hide turtle
screen = Screen()
tim.colormode(255)
turtle_ycor = 0

def tim_moving():
    for _ in range(10):
        tim.pd(); tim.dot(20, random.choice(colour_list)); tim.pu(); tim.fd(50)

for _ in range(10):
    tim_moving()
    turtle_ycor += 50
    tim.teleport(0, turtle_ycor)

screen.exitonclick()

#solution code for Hirst Painting project part 2
#import turtle as turtle_module

#turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(colour_list))
#     tim.forward(50)
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = turtle_module.Screen()
# screen.exitonclick()