def calculate_score(results):
    score = 0
    for result in results:
        if result == True:
            score = score + 1
    return score

def show_result(score, total):
    print("Score:", score, "/", total)
    percentage = (score / total) * 100
    print("Percentage:", percentage)

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")