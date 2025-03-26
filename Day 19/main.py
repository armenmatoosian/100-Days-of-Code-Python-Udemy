import turtle
from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
is_race_on = False
screen = Screen()

# #my code for Etch-A-Sketch challenge
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def move_counter_clockwise():
#     tim.left(5)
# def move_clockwise():
#     tim.right(5)
# def clear():
#     tim.reset()
#
#
# screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="a",fun=move_counter_clockwise)
# screen.onkey(key="d",fun=move_clockwise)
# screen.onkey(key="c",fun=clear)
#
# screen.exitonclick()

# #solution code for Etch-A-Sketch challenge
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, "Up")
# screen.onkey(move_backwards, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")
# screen.onkey(clear, "c")
#
# screen.exitonclick()

# shared code for Turtle Race project
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# # my code for Turtle Race project
# tim_red = Turtle(shape="turtle")
# tim_orange = Turtle(shape="turtle")
# tim_yellow = Turtle(shape="turtle")
# tim_green = Turtle(shape="turtle")
# tim_blue = Turtle(shape="turtle")
# tim_purple = Turtle(shape="turtle")
#
# tim_red.color(colours[0])
# tim_orange.color(colours[1])
# tim_yellow.color(colours[2])
# tim_green.color(colours[3])
# tim_blue.color(colours[4])
# tim_purple.color(colours[5])
#
# tim_red.teleport(x=-230, y=-100)
# tim_orange.teleport(x=-230, y=-62)
# tim_yellow.teleport(x=-230, y=-24)
# tim_green.teleport(x=-230, y=24)
# tim_blue.teleport(x=-230, y=62)
# tim_purple.teleport(x=-230, y=100)

# solution (and some shared) code for Turtle Race project
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint (0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()