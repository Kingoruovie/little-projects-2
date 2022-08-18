from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Created a screen to display the turtles created
screen = Screen()
# Change the screen color to black
screen.bgcolor("red")
# Set up the screen size to a particular size to have control the screen length and width
screen.setup(width=600, height=600)
# A title was created fo the snake game
screen.title("SNAKE GAME")
# A listen key to make keyboard work with turtle
screen.listen()
# Shuts down the animation mode of the screen, avoiding seeing individual movement of the turtle
screen.tracer(0)

# Created the object snake as the snake body and head combined
snake = Snake()
# The food object, a turtle to be eaten by the snake
food = Food()
# Keeping track of the score by the object score
scoreboard = Scoreboard()

# A collection of keybindings for turtle control
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# A boolean to hold and change whenever any set of conditions are satisfied
game_is_on = True

# A while loop to engender constant movement of turtle except a failure of some sort
while game_is_on:
    # An update on screen to bring back to the screen the turtles since the tracer had been switched off
    screen.update()
    # A time method to control the speed of the turtle
    time_increase = 0.1
    time.sleep(time_increase)
    # Movement method define in the snake class to define control over turtle
    snake.move()
    # Trying to increase the or speed of the turtle based on the score had
    if scoreboard.score == 10:
        time_increase = 0.01
    elif scoreboard.score == 30:
        time_increase = 0.001
    elif scoreboard.score == 45:
        time_increase = 0.0001

    # Detection of food and extension after the consumption of the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_the_score()
    # Collision of the wall analysis
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.high_score_checker()
        snake.reset_snake_position()
    # Collision with the tail analysis
    for turtle in snake.list_of_turtle[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.high_score_checker()
            snake.reset_snake_position()

screen.exitonclick()
