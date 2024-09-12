import html


class QuizBrain:
    """Class for presenting questions and controlling the logic flow of the quiz"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_question.text = html.unescape(current_question.text)
        self.question_number += 1
        user_answer = input(
            f"\nQ.{self.question_number}: {current_question.text}. (True/False)?: "
        )
        correct = self.check_answer(user_answer, current_question)
        self.calculate_score(correct)
        return

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            print("You got it!")
            return True
        print(f"Incorrect, the correct answer was {current_question.answer}")

    def are_questions_remaining(self):
        return self.question_number < len(self.question_list)

    def calculate_score(self, correct):
        if correct:
            self.score += 1
        print(f"Your score is {self.score}/{self.question_number}")
