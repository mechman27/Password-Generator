from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\n Your final score is: {quiz.score}/{quiz.current_question_index}\n you got {quiz.score/quiz.current_question_index*100 :.2f}% correct")