"""
This program reads user names from a file and customizes letters as per the user names.
If you get "FileNotFoundError", try replacing the relative file/folder paths with absolute paths.
"""


def main():
    # Text to replace in the letter
    PLACEHOLDER = '[name]'

    with open('./Input/Names/invited_names.txt') as names_data:
        # Read the user names into a list
        names = names_data.readlines()

    with open('./Input/Letters/starting_letter.txt', mode='r') as letter_data:
        # Read the data of the starting letter
        letter = letter_data.read()

        for name in names:
            # Remove extra characters
            stripped_name = name.strip()

            # Replace the placeholder with the user name
            subjective_letter = letter.replace(PLACEHOLDER, stripped_name)

            # Write the letter output customized for an user
            path = './Output/ReadyToSend/'
            with open(f'{path}letter_for_{stripped_name}.txt', mode='w') as letter_write:
                letter_write.write(subjective_letter)

        print(f'Letter customization completed successfully. The letters are at the path: "{path}"')


if __name__ == '__main__':
    main()
