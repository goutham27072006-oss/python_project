questions_list = ["What is the capital of India?",
                  "Which language is used for Python programming?",
                  "What is 5 + 3?"]

answers_list = ["Delhi",
                "Python",
                "8"]

def show_questions():
    count = 1
    for question in questions_list:
        print(str(count) + ". " + question)
        count = count + 1

def get_question(index):
    if index >= 0 and index < len(questions_list):
        return questions_list[index]
    return "Invalid Question Index"