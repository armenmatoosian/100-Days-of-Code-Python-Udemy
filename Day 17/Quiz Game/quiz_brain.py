from itertools import count
# solution code
class QuizBrain:
    def __init__(self, q_list):
         self.question_number = 0
         self.score = 0
         self.question_list = q_list

    # TODO: checking if we're at the end of the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    #TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # TODO: checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


# my code - almost right, and might still work
# class QuizBrain:
#    def __init__(self, question_number, question_list):
#         self.question_number = 0
#         self.question_list = question_bank[question_number]
#
#     def still_has_questions(self):
#         if self.question_number >= len(self.question_list):
#             return True
#         else:
#             return False
#
#     #TODO: asking the questions
#     def next_question(self):
#         quiz_number = QuizBrain(question_bank).question_number
#         self.next_question = input(f"Q.{}")

