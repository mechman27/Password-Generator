class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.current_question_index = 0
        self.score = 0


    def still_has_questions(self):
        return len(self.question_bank) > self.current_question_index
            

    def next_question(self):
        question = self.question_bank[self.current_question_index]
        self.current_question_index += 1
        user_selection = input(f"Q.{self.current_question_index}: {question.text} True or False:")
        self.check_answer(user_selection, question.answer)
        print(f"your current score is: {self.score}/{self.current_question_index}")

    
    def check_answer(self,user_input, correct_answer):
        if correct_answer.lower() == user_input.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer is: {correct_answer}")