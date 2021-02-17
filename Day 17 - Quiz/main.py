"""
This file drives the execution of quiz by using all the classes
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    """
    Creates instances of the classes to implement the quiz
    :return: nothing
    """
    question_bank = []
    for question in question_data:
        new_quest = Question(question['question'], question['correct_answer'])
        question_bank.append(new_quest)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print('You have completed the quiz')
    print(f'The final score is: {quiz.score}/{len(quiz.question_list)}')


if __name__ == '__main__':
    main()
