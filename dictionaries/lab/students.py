command = input()
students = {}
while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in students:
        students[course] = {}
    students[course][id] = name
    command = input()
course = ' '.join(command.split("_"))
for key, value in students.items():
    if course == key:
        for id, name in value.items():
            print(f"{name} - {id}")
