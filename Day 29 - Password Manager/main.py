"""
This program implements a Password Manager
"""

import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates random secure password
    :return: nothing
    """
    ent_password.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    pass_list = numbers_list + symbols_list + letters_list

    shuffle(pass_list)
    pass_string = ''.join(pass_list)

    ent_password.insert(0, pass_string)
    copy(pass_string)
    messagebox.showinfo(title='Password Copied', message='Generated password copied. Ready to paste!')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    """
    Adds password data to the data file
    :return:
    """
    website = ent_website.get()
    email = ent_email.get()
    password = ent_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Missing Details', message='You have left some fields blank. Please fill all the '
                                                              'fields to proceed!')
    else:
        is_correct = messagebox.askokcancel(title=website,
                                            message=f'The entered details are:\nEmail: {email}\nPassword: {password}\nIs '
                                                    f'this correct information to save to the file?')
        if is_correct:
            with open('data.txt', 'a') as f:
                f.write(f'{website} | {email} | {password}\n')
                ent_website.delete(0, 'end')
                ent_password.delete(0, 'end')
            messagebox.showinfo(title='Success', message='Information saved successfully')


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

lbl_website = tk.Label(text='Website:')
lbl_website.grid(column=0, row=1)

lbl_email = tk.Label(text='Email/Username:')
lbl_email.grid(column=0, row=2)

lbl_password = tk.Label(text='Password:')
lbl_password.grid(column=0, row=3)

ent_website = tk.Entry(width=52)
ent_website.focus()
ent_website.grid(column=1, row=1, columnspan=2)

ent_email = tk.Entry(width=52)
ent_email.grid(column=1, row=2, columnspan=2)

ent_password = tk.Entry(width=21)
ent_password.grid(column=1, row=3, sticky='ew')

btn_generate = tk.Button(text='Generate Password', command=generate_password)
btn_generate.grid(column=2, row=3)

btn_add = tk.Button(text='Add', width=36, command=add_data)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
