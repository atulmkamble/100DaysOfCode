"""
This file implements the QuizInterface class for UI of Quizzler game
"""

import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Hello',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = tk.PhotoImage(file='./images/true.png')
        self.btn_correct = tk.Button(image=correct_image, highlightthickness=0, command=self.check_correct)
        self.btn_correct.grid(row=2, column=0)

        wrong_image = tk.PhotoImage(file='./images/false.png')
        self.btn_wrong = tk.Button(image=wrong_image, highlightthickness=0, command=self.check_wrong)
        self.btn_wrong.grid(row=2, column=1)

        self.lbl_score = tk.Label(text=f'Score: {0}', fg='white', bg=THEME_COLOR)
        self.lbl_score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f'Score: {self.quiz.score}/{len(self.quiz.question_list)}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,
                                   text=f'{q_text}')
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f'You have reached the end of quiz.'
            )
            self.btn_correct.config(state='disabled')
            self.btn_wrong.config(state='disabled')

    def check_correct(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def check_wrong(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
