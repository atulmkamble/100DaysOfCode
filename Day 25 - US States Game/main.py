import turtle
import pandas as pd
from display_states import DisplayStates


def main():
    """
    Implements the U.S. States game functionality
    :return: nothing
    """
    screen = turtle.Screen()
    screen.title('U.S. States Game')

    # Add image to screen
    image = 'blank_states_img.gif'
    screen.addshape(image)
    turtle.shape(image)

    guessed_states = []
    df = pd.read_csv('50_states.csv')
    # Convert the states DataFrame column to list
    states_list = df['state'].to_list()

    # While all the states are not guessed, repeat the loop
    while len(guessed_states) < 50:
        ans_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                     prompt="What's another state's name? Type 'exit' to quit").title()
        if ans_state == 'Exit':
            break
        # The state name should be as per the states input file and the state name should not be repeated
        elif ans_state in states_list and ans_state not in guessed_states:
            guessed_states.append(ans_state)

            # Fetch the state row with its coordinate on the image
            current_state_row = df[df['state'] == ans_state]
            new_state = DisplayStates()
            x = int(current_state_row['x'])
            y = int(current_state_row['y'])

            # Mark the position of the state on the map
            new_state.mark_state(x, y, ans_state)

    if len(guessed_states) == 50:
        print('Congratulations! You guessed all the states correctly!')
    else:
        # Output missing state to a CSV file
        missing_states = pd.DataFrame(list(set(states_list) - set(guessed_states)), columns=['State Name'])
        filename = 'states_to_learn.csv'
        missing_states.to_csv(filename)
        print(f'The states that you missed are written to "{filename}" file. Learn and improve!')


if __name__ == '__main__':
    main()
