

def grade(current_grade):
    grade_word = None
    if 2.00 <= current_grade <= 2.99:
        grade_word = "Fail"
    elif 3.00 <= current_grade <= 3.49:
        grade_word = "Poor"
    elif 3.50 <= current_grade <= 4.49:
        grade_word = "Good"
    elif 4.50 <= current_grade <= 5.49:
        grade_word = "Very Good"
    else:
        grade_word = "Excellent"
    return grade_word


score = float(input())
print(grade(score))
