def main():
    score = float(input("Enter score: "))
    evaluation = evaluate_score(score)
    print(evaluation)


def evaluate_score(score):
    if score > 100:
        evaluation = "Invalid score"
    elif score >= 90:
        evaluation = "Excellent"
    elif score >= 50:
        evaluation = "Passable"
    elif score >= 0:
        evaluation = "Bad"
    else:
        evaluation = "Invalid score"
    return evaluation


main()
