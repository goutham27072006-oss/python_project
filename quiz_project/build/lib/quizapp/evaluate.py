from quizapp.questions import answers_list

def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    return False

def evaluate_all(user_answers):
    results = []

    for i in range(len(user_answers)):
        result = check_answer(user_answers[i], answers_list[i])
        results.append(result)
    return results