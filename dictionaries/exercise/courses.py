student_data = {}
command = input()
while command != "end":
    course, student = command.split(" : ")
    if course not in student_data:
        student_data[course] = []
    student_data[course].append(student)
    command = input()
for course in student_data.keys():
    print(f"{course}: {len(student_data[course])}")
    for student in student_data[course]:
        print(f"-- {student}")
