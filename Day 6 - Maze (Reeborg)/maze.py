"""
This program guides/navigates the Reeborg robot to the exit of the maze (similar to Karel the Robot).
This code only works at the link:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
You can paste this code in the Python code tab at the link above and watch the robot in action.
"""


# The robot does not have turn right feature. This function adds this capability.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Handle the deadlock case where the robot is stuck in a square loop
while front_is_clear():
    move()
turn_left()

# Stick with the right edge of the maze and continue towards the target. If stuck only then turn to the left
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
