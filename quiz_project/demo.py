from quizapp.questions import show_questions
from quizapp.evaluate import evaluate_all
from quizapp.score import calculate_score
from quizapp.score import show_result

print("----- QUIZ APPLICATION -----")
show_questions()
user_answers = []

answer1 = input("Enter answer for Question 1: ")
user_answers.append(answer1)

answer2 = input("Enter answer for Question 2: ")
user_answers.append(answer2)

answer3 = input("Enter answer for Question 3: ")
user_answers.append(answer3)

results = evaluate_all(user_answers)
score = calculate_score(results)
show_result(score, len(results))