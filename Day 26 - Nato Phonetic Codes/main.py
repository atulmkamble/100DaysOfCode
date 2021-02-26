# Import required libraries
import pandas as pd
from art import logo


def main():
    print(logo)
    # Read the file
    df = pd.read_csv('nato_phonetic_alphabet.csv')

    # Create dictionary of letters and corresponding codes
    nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

    # Get the user input and create codes corresponding to letters
    name = input('Enter your name: ').upper()
    code_words = [nato_dict[char] for char in name if char in nato_dict.keys()]
    print('Nato Phonetic Codes:')
    print(code_words)


if __name__ == '__main__':
    main()
