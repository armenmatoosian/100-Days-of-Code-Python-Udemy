from turtle import Turtle

#my code for Pong: Create a Paddle that responds to Key Presses
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_COLOUR = "white"
UP = 90
DOWN = 360
# RIGHT_PADDLE_X_START_POSITION = 725
# RIGHT_PADDLE_Y_START_POSITION = 0

class Paddles(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOUR)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.seth(90)

    def up(self):
        if self.seth == 270:
            self.seth(90)
        self.forward(20)

    def down(self):
        if self.seth == 90:
            self.seth(270)
        self.backward(20)

#solution code for Pong: Create Another Paddle
