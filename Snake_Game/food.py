from turtle import Turtle
from random import randint


class Food(Turtle):
    """Creating the food"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        """Randomizing the creation of the turtle on the screen"""
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)
