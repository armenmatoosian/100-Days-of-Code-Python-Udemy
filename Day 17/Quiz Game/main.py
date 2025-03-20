from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# solution code, works without duplicating 🙃
for question in question_data:
   question_text = question["question"]
   question_answer = question["correct_answer"]
   new_question = Question(question_text, question_answer)
   question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions() is True:
   quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")


# my code - seems to work but prints many duplicates of the questions, not sure why
# question = Question(q_text= "", q_answer= "")
#
# for text, answer in question_data:
#    question.text = question_data
#    question.answer = question_data
#    question_bank.append(question.text)
#    question_bank.append(question.answer)
#
# print(question_bank)