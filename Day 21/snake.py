# # my code - could not get it to work, was thinking of moving first for loop to its own method but did not know how
# class Snake:
#     def __init__(self, starting_positions, segments, new_segments):
#         self.starting_positions = starting_positions
#         self.segments = segments
#         self.new_segments = new_segments
#
#         from turtle import Turtle, Shape
#
#         def move(self):
#             for position in starting_positions:
#                 new_segment = Turtle("square")
#                 new_segment.color("white")
#                 new_segment.penup()
#                 new_segment.goto(position)
#                 segments.append(new_segment)
#
#                 for seg_num in range(len(segments) - 1, 0, -1):
#                     new_x = segments[seg_num - 1].xcor()
#                     new_y = segments[seg_num - 1].ycor()
#                     segments[seg_num].goto(new_x, new_y)
#                 segments[0].forward(20)

# solution code
from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        #solution code
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #solution code for Snake Game Part 2: Detect Collisions with Your Own Tail
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # solution code for Snake Game Part 2: Detect Collisions with Your Own Tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

# my code and solution code for Snake Game Part 1: Control the Snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)