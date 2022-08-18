from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """A snake crate that produces the beginning three squared snake"""
    def __init__(self):
        self.list_of_turtle = []
        self.create_snake()
        self.head = self.list_of_turtle[0]

    def create_snake(self):
        """Makes the beginning body of the snake"""
        for position in STARTING_POSITION:
            self.add_new_turtle(position)

    def add_new_turtle(self, position):
        """Creates every needed turtle for the snake body"""
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.setposition(position)
        self.list_of_turtle.append(new_turtle)

    def extend(self):
        """The extension of the snake body after the collision with food detected"""
        new_turtle_position = self.list_of_turtle[-1].position()
        self.add_new_turtle(new_turtle_position)

    def move(self):
        """A special movement process proposed by Angela Yu based on the replacement of the position preoccupied
        by the turtle ahead"""
        for made_turtle_number in range(len(self.list_of_turtle) - 1, 0, -1):
            new_x = self.list_of_turtle[made_turtle_number - 1].xcor()
            new_y = self.list_of_turtle[made_turtle_number - 1].ycor()
            self.list_of_turtle[made_turtle_number].goto(new_x, new_y)
        self.list_of_turtle[0].forward(20)

    def reset_snake_position(self):
        for segment in self.list_of_turtle:
            segment.goto(1000, 1000)
        self.list_of_turtle.clear()
        self.create_snake()
        self.head = self.list_of_turtle[0]

    # The direction of movement
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
