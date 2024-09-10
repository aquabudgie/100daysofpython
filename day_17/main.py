from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from api_data import ApiData

question_list = []
question_data = ApiData("https://opentdb.com/api.php?amount=10&type=boolean")

for question in question_data.question_list:
    q = Question(question["question"], question["correct_answer"])
    question_list.append(q)


quiz = QuizBrain(question_list)
while quiz.are_questions_remaining():
    quiz.next_question()

print("\n\n\nYou've completed the quiz")
print(f"\nYour final score was: {quiz.score}/{quiz.question_number}")