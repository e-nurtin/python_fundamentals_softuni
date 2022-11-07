def check_validity(contest_data, contest, password):
    if contest in contest_data.keys():
        if contest_data[contest] == password:
            return True


def update_data(name, contest, points, students_data):
    if contest not in students_data[name]:
        students_data[name][contest] = points
    elif students_data[name][contest] < points:
        students_data[name][contest] = points
    return students_data


def get_contest_data(data):
    command = input()
    while command != "end of contests":
        data.extend(command.split(':'))
        command = input()
    contest_data = {data[index]: data[index + 1] for index in
                    range(0, len(data), 2)}
    data.clear()
    return contest_data


def get_student_data(data):
    command = input()
    while command != "end of submissions":
        data.append(command)
        command = input()
    return data


def process_submission(current, students):
    contest, password, name, points = current[0], current[1], current[2], \
                                      current[3]
    if check_validity(contest_data, contest, password):
        if name not in student_data:
            student_data[name] = {}
        update_data(name, contest, points, students)
    return students


def get_best_student(students):
    max_points = 0
    max_point_name = ""
    for name, contests in students.items():
        current_points = sum(contests.values())
        if current_points > max_points:
            max_point_name = name
            max_points = current_points
    return max_point_name, max_points


data = []
student_data = {}

contest_data = get_contest_data(data)
data = get_student_data(data)

for submission in data:
    current_submission = [int(x) if x.isdigit() else x for x in
                          submission.split('=>')]
    student_data = process_submission(current_submission, student_data)

# sort the dictionary in alphabetical order
student_data = dict(sorted(student_data.items()))

# get best student name and points
name, points = get_best_student(student_data)

# print in desired output
print(f"Best candidate is {name} with total {points} points.")
print("Ranking:")
for name in student_data:
    print(name)
    ordered = dict(sorted(student_data[name].items(), key=lambda item: item[1],
                          reverse=True))
    for contest, points in ordered.items():
        print(f"#  {contest} -> {points}")


#  sorting by value
# dict(sorted(student_data['Tanya'].items(), key=lambda item: item[1], reverse= True))
