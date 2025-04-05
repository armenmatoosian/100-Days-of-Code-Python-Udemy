from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#my code for Create the Player Behaviour, very close solution code
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.new_y = self.ycor()

    # my code for Create the Player Behaviour, very close solution code
    def move(self):
        self.forward(MOVE_DISTANCE) #solutiion used this, interestingly enough, as solutions usually use goto()

    # my code Detect when the PLayer has reached the other side
    def reset_position(self):
        self.goto(STARTING_POSITION)