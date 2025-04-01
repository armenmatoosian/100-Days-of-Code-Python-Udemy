from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.new_y = self.ycor()

    def move(self):
        # self.forward(MOVE_DISTANCE)
        self.new_y += MOVE_DISTANCE
        self.goto(0, self.new_y)