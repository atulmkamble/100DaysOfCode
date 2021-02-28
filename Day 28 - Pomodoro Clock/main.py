"""
This program implements a Pomodoro GUI Application
"""

import tkinter as tk
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    lbl_timer.config(text='Timer', fg=GREEN)
    lbl_chk_marks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_min)
        lbl_timer.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        lbl_timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        lbl_timer.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(floor(reps / 2)):
            marks += '✔'
        lbl_chk_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro Clock')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

lbl_timer = tk.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
lbl_timer.grid(column=1, row=0)

btn_start = tk.Button(text='Start', command=start_timer, highlightthickness=0)
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text='Reset', command=reset_timer, highlightthickness=0)
btn_reset.grid(column=2, row=2)

check = ''
lbl_chk_marks = tk.Label(text=check, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
lbl_chk_marks.grid(column=1, row=3)

window.mainloop()
