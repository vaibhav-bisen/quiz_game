
class QuizBrain:
  def __init__(self, a_list):
    self.question_number = 0
    self.question_list = a_list
    self.score = 0

  def still_has_question(self, question_list):
    return self.question_number < len(self.question_list)
   
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_ans(user_ans, current_question.ans)

  def check_ans(self, user_ans, correct_ans):
    if user_ans.lower() == correct_ans.lower():
      print("You got right!")
      self.score += 1 

    else:
      print("That's wrong")
  
    print(f"The correct answer ws: {correct_ans}.")
    print(f"Your current scoreos: {self.score}/{self.question_number}\n")

