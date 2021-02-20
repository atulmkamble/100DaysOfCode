from turtle import Turtle

# Initialize constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    This class creates the snake components to be displayed on screen
    """

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        """
        Create the snake object by using Turtle class
        :return: nothing
        """
        for position in STARTING_POSITIONS:
            new_square = Turtle('square')
            new_square.color('white')
            new_square.penup()
            new_square.goto(position)
            self.snake_list.append(new_square)

    def move(self):
        """
        Moves the blocks that form the snake. Every block takes the position of the block prior to it.
        The last block is moved separately outside the for loop.
        :return: nothing
        """
        for square_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[square_num - 1].xcor()
            new_y = self.snake_list[square_num - 1].ycor()
            self.snake_list[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Changes the direction of the snake upwards
        :return: nothing
        """
        # Don't let the snake go up if it is currently heading down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the direction of the snake downwards
        :return: nothing
        """
        # Don't let the snake go down if it is currently heading up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the direction of the snake leftwards
        :return: nothing
        """
        # Don't let the snake go left if it is currently heading right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the direction of the snake rightwards
        :return: nothing
        """
        # Don't let the snake go right if it is currently heading left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
