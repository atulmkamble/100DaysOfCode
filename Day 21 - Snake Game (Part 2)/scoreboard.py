from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.display_score()

    def update_score(self):
        """
        Updates the score and displays it on the screen
        :return: nothing
        """
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        """
        Displays the score by using the write function
        :return: nothing
        """
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Makes the game quit
        :return: nothing
        """
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)
