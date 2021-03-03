"""
This program implements a French Flash Card Game
"""

import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# Tracks the current word from the file
current_card = {}
# Stores the entire list of words from file
word_list = {}

try:
    # Read the words to learn if this app has been used before
    df = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    # Read the entire list of words for the first time
    original_data = pd.read_csv('./data/french_words.csv')
    word_list = original_data.to_dict(orient='records')
else:
    word_list = df.to_dict(orient='records')


def get_word():
    """
    Get the next French word from the word list
    :return: nothing
    """
    global current_card, flip_timer
    # Cancels the previous timer if there are multiple clicks
    window.after_cancel(flip_timer)

    current_card = choice(word_list)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')

    # Set the current time for new word
    flip_timer = window.after(3000, get_meaning)


def get_meaning():
    """
    Flips the card and give the English meaning of the French word
    :return: nothing
    """
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


def is_known():
    """
    Removes known words from the list and saves the new list to a file
    :return: nothing
    """
    word_list.remove(current_card)
    data = pd.DataFrame(word_list)
    data.to_csv('./data/words_to_learn.csv', index=False)
    get_word()


# Window Object
window = tk.Tk()
window.title('French Flash Card Game')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, get_meaning)

# Canvas for card
canvas = tk.Canvas(width=800, height=526)
front_image = tk.PhotoImage(file='./images/card_front.png')
back_image = tk.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 260, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# X and Y positions are relative to canvas size
title_text = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 280, text='Word', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_image = tk.PhotoImage(file='./images/right.png')
btn_correct = tk.Button(image=correct_image, highlightthickness=0, command=is_known)
btn_correct.grid(row=1, column=1)

wrong_image = tk.PhotoImage(file='./images/wrong.png')
btn_wrong = tk.Button(image=wrong_image, highlightthickness=0, command=get_word)
btn_wrong.grid(row=1, column=0)

# Call to replace default text
get_word()

window.mainloop()
