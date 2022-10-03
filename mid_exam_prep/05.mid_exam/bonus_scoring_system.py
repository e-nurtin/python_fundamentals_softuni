from math import ceil

number_of_students = int(input())
course_lectures = int(input())
additional_bonus = int(input())

max_points = 0
max_attendances = 0
for student in range(number_of_students):
    student_attendances = int(input())
    current_student_points = (student_attendances / course_lectures) *\
                             (5 + additional_bonus)
    if current_student_points > max_points:
        max_points = current_student_points
        max_attendances = student_attendances

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {max_attendances} lectures.")
