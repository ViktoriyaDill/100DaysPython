from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


game = QuizBrain(question_bank)
while game.still_has_question():
    game.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {game.score}/{game.question_number}")



