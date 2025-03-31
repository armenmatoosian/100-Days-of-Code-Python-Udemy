from random import randint
from turtle import Turtle

#my code and solution code for Pong: Create the Ball Class and Make the Ball Move
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # # my code for Pong: Add the Ball Bouncing Logic
        # self.new_x = 0 #my code for Pong: Add the Ball Bouncing Logic
        # self.new_y = 0 #my code for Pong: Add the Ball Bouncing Logic
        # self.direction = randint(0, 360) #my code for Pong: Add the Ball Bouncing Logic
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # #my code for Pong: Create the Ball Class and Make the Ball Move
    # #this code is not dynamic, but it does move the ball to the top right corner per the challenge
    # def move(self):
    #     self.speed("slow")
    #     self.forward(1)
    #     self.setheading(40)

    #solution code for Pong: Create the Ball Class and Make the Ball Move and Add the Ball Bouncing Logic
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # #my code for Pong: Add the Ball Bouncing Logic
    # def move(self):
    #     self.seth(self.direction)
    #     self.forward(10)
    #     self.new_x = self.xcor()
    #     self.new_y = self.ycor()

    #solution code for Pong: Add the Ball Bouncing Logic and How to Detect Collisions with the Paddle
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # my code for Pong: How to Detect when the Ball goes out of Bounds - same as solution code
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
        self.y_move *= -1