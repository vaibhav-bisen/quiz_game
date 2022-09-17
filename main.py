from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data:
  question_text = question["text"]
  question_ans = question["answer"]
  new_que = Question(question_text, question_ans)
  questions_bank.append(new_que)


quiz = QuizBrain(questions_bank)

while quiz.still_has_question(questions_bank):
  quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(questions_bank)}")