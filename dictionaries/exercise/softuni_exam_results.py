def check_points(student, current_points):
    if student not in exam_results:
        exam_results[student] = 0
    if exam_results[student] < current_points:
        exam_results[student] = current_points


def count_language_submissions(language):
    if language not in language_submissions:
        language_submissions[language] = 0
    language_submissions[language] += 1


def ban_user(student):
    del exam_results[student]


language_submissions = {}
exam_results = {}
command = input()
while command != "exam finished":
    name, *info = [int(x) if x.isdigit() else x for x in
                   command.split('-')]
    if info[0] == "banned":
        ban_user(name)
    else:
        check_points(name, info[1])
        count_language_submissions(info[0])

    command = input()

print("Results:")
for student, points in exam_results.items():
    print(f"{student} | {points}")
print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")