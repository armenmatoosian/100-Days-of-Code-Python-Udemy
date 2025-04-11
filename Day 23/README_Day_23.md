**Day**: 23\
**Content**: Turtle Crossing Game Capstone Project

This is my attempt at Day 23. There are three difficulty levels to choose from for this day's project.

- Difficulty Normal 😎: Use all Steps to complete the project.
- Difficulty Hard 🤔: Use only Steps 1 and 2 to complete the project.
- Difficulty Expert 🤯: Only use Step 1 to complete the project.

I chose to start with Hard, with Step 2 comprising a breakdown of the project provided by the course. I got really stuck at step 4, Create the Car Behaviour, and referred to the course video, which brings me down to normal difficulty. I was able to work through the remaining three steps pretty easily, with some help from Claude for step 5 and referencing code from prior Days. Some of my code is slightly different from the solution code but the functionality is the same. The breakdown of all the steps is below. 

My chat with Claude for Day 23 can be found [here](https://claude.ai/share/df380df2-0786-4213-863f-96265cc09a8b).

Here are the steps provided by the course:
- Step 1 - Check out how the game play works.


- Step 2 - Break down the problem.


- Step 3 - Create the Player behaviour.
  - Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

- Step 4 - Create the Car behaviour
  - Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.


- Step 5 - Detect when the Turtle collides with a Car *squish*.
  - Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.


- Step 6 - Detect when the Player has reached the other side.
  - Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.
 

- Step 7 - Add the Scoreboard and Game Over sequence.
  - Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.