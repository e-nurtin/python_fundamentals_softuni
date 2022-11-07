count_of_grades = int(input())
student_grades = {}
poor_students = []
avg_grade = 4.50
for i in range(count_of_grades):
    student = input()
    grade = float(input())
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)
for student, grade in student_grades.items():
    students_avg = sum(student_grades[student]) / len(student_grades[student])
    if students_avg >= avg_grade:
        print(f"{student} -> {students_avg:.2f}")
    else:
        poor_students.append(student)
for student in poor_students:
    del student_grades[student]

