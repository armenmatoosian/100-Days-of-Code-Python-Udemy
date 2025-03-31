from turtle import Screen, Turtle
from paddles import Paddles
from paddle import  Paddle
from ball import Ball
import time
from scoreboard import Scoredboard

#my code for Pong: Set up the Main Screen (matches solution code)
screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #solution code for Pong: Create a Paddle that responds to Key Presses

# #my code for Pong: Create a Paddle that responds to Key Presses
# right_paddle = Paddles(725, 0)
# # left_paddle = Paddles(-725, 0)
#
# screen.listen()
# screen.onkey(right_paddle.up, "Up")
# screen.onkey(right_paddle.down,"Down")
# # screen.onkey(left_paddle.up,"Down")
# # screen.onkey(left_paddle.down,"Down")

#solution code for Pong: Create Another Paddle
r_paddle = Paddle(725, 0) #solution code has a tuple here, which doesn't work for me; (350, 0) also doesn't work for me
l_paddle = Paddle(x=-725, y=0)
ball = Ball()
scoreboard = Scoredboard()

#my code for Pong: Create Another Paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#solution code for Pong: Create a Paddle that responds to Key Presses
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    # #my code for Pong: Add the Ball Bouncing Logic
    # if ball.new_y > 300 or ball.new_y < -300: #my code for Pong: Add the Ball Bouncing Logic
    #     ball.direction += 90 #my code for Pong: Add the Ball Bouncing Logic

    #solution code for Pong: Add the Ball Bouncing Logic
    if ball.ycor() > 625 or ball.ycor() < -625:
        ball.bounce_y()

    # solution code for Pong: How to Detect Collisions with the Paddle
    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    #my code for Pong: How to Detect when the Ball goes out of Bounds - same as solution code
    #Detect R paddle misses
    if ball.xcor() >= 725:
        ball.reset_position()
        scoreboard.l_point()
    #Detect L paddle misses
    elif ball.xcor() <= -725:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()