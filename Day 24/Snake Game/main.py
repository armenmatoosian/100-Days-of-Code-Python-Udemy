# # shared code for Snake Game
# from turtle import Screen, Turtle, Shape
# import time
#
# screen = Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# # my code for Snake Game Part 1: Screen Setup and Creating a Snake Body
# # I was on the right track with the for loop and snake list, but missed with positioning and loop logic, also did not use tuples
# snake = []
# snake_x_position = 0
# snake_y_position = 0
# snake_pieces = 3
#
# for body_part in range(0, snake_pieces):
#     snake_body = Turtle()
#     snake_body.shape("square")
#     snake_body.shapesize(stretch_len=1,stretch_wid=1)
#     snake_body.color("white")
#     snake_body.setpos(snake_x_position, snake_y_position)
#     snake_x_position += -20
#     snake_y_position += 0
#
# snake.append(snake_body)

# # solution code for Snake Game Part : Screen Setup and Creating a Snake Body
# starting_positions = [(0,0),(-20,0),(-40,0)]
#
# for position in starting_positions:
#     newsegment = Turtle("square")
#     newsegment.color("white")
#     newsegment.goto(position)

# # course code for Snake Game Part 1: Move the Snake
# starting_positions = [(0,0),(-20,0),(-40,0)]
#
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)

# my code for Snake Game Part 1: Create a Snake Class and Move to OOP
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # scoreboard.scoreboard() #my code
    scoreboard.update_scoreboard()  # solution code, but I put this here so there is a scoreboard even when score is 0

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # scoreboard.score_refresh() #my code
        scoreboard.increase_score() #solution code

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False # code from Day 24: Add a High Score to the Snake Game
        #scoreboard.game_over() # code from Day 24: Add a High Score to the Snake Game
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail - original code
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance() < 10:
    #         # game_is_on = False # code from Day 24: Add a High Score to the Snake Game
    #         # scoreboard.game_over() # code from Day 24: Add a High Score to the Snake Game
    #         scoreboard.reset()
    #         snake.reset()

    #Detect collision with tail - code with slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False # code from Day 24: Add a High Score to the Snake Game
            # scoreboard.game_over() # code from Day 24: Add a High Score to the Snake Game
            scoreboard.reset() # code from Day 24: Add a High Score to the Snake Game
            snake.reset() # code from Day 24: Add a High Score to the Snake Game


screen.exitonclick()