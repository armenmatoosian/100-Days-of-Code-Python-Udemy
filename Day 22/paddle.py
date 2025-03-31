from turtle import Turtle

#my code for Pong: Create Another Paddle
class Paddle(Turtle):
    def __init__(self, x , y):
        super().__init__()
        #solution code for Pong: Create a Paddle that responds to Key Presses
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
        self.new_y = self.ycor()

    #my code and solution code for Pong: Create Another Paddle
    def go_up(self):
        self.new_y += 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y -= 20
        self.goto(self.xcor(), self.new_y)