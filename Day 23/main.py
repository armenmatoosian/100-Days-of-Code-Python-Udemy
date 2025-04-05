import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
# #my code for Create the Car Behaviour
# cars = CarManager()
# all_cars = []
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen() #my code for Create the Player Behaviour, same as solution code
screen.onkey(player.move, "Up") #my code for Create the Player Behaviour, same as solution code

# #my code for Create the Car Behaviour
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     for new_car in range(6):
#         all_cars.append(cars.new_car)
#         cars.move()

# solution code for Create the Car Behaviour
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # my code for Detect when the Turtle collides with a Car *squish*, with Claude's help
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over() #my code for Add the Scoreboard and Game Over sequence

    # my code Detect when the Player has reached the other side
    if player.ycor() >= FINISH_LINE_Y:
        car_manager.increase_speed()
        player.reset_position()
        scoreboard.increase_level() #my code for Add the Scoreboard and Game Over sequence

screen.exitonclick()