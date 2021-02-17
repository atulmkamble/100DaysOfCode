"""
This file implements the logic of quiz
"""


class QuizBrain:
    """
    This class implements the quiz functionality
    """

    def __init__(self, question_bank):
        """
        Constructor
        :param question_bank: Questions database
        """

        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        """
        Get the next question and check the answer of the current question
        :return: nothing
        """

        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer.casefold()
        response = input(f'Q.{self.question_number + 1}: {current_question} (True/False)?: ').casefold()
        self.question_number += 1
        self.check_answer(response, current_answer)

    def still_has_questions(self):
        """
        If the questions database is not exhausted, get another question
        :return: true is there are more questions in the database
        """

        return self.question_number < len(self.question_list)

    def check_answer(self, response, current_answer):
        """
        Checks the user's answer
        :param response: user's answer
        :param current_answer: answer from the database
        :return: nothing
        """

        if response == current_answer:
            print('You got it right!')
            self.score += 1
        else:
            print('That is wrong.')
        print(f'The correct answer was: {current_answer}')
        print(f'You current score is: {self.score}/{self.question_number}\n')
