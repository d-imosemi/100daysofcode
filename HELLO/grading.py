student_score = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Dreco': 74,
    'Neville': 62,
}

student_grades = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'exceeds Expectation'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)