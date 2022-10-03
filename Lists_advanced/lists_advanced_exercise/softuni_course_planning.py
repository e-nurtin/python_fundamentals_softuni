def add(lesson):
    if lesson not in course_plan:
        course_plan.append(lesson)


def insert(lesson, index_to_insert):
    if lesson not in course_plan:
        course_plan.insert(index_to_insert, lesson)


def remove(lesson):
    if lesson in course_plan:
        index_of_lesson = course_plan.index(lesson)
        del course_plan[index_of_lesson]
        if check_for_exercise(index_of_lesson):
            del course_plan[index_of_lesson]


def swap(lesson_1, lesson_2):
    if lesson_1 in course_plan and lesson_2 in course_plan:
        index_1 = course_plan.index(lesson_1)
        index_2 = course_plan.index(lesson_2)
        course_plan[index_1], course_plan[index_2] = course_plan[index_2], \
                                                     course_plan[index_1]
        if check_for_exercise(index_1):
            course_plan.insert(index_2 + 1, course_plan.pop(index_1 + 1))
        if check_for_exercise(index_2):
            course_plan.insert(index_1 + 1, course_plan.pop(index_2 + 1))


def check_for_exercise(index_1):
    try:
        if 'Exercise' in course_plan[index_1 + 1]:
            return True
    except IndexError:
        return False


def exercise(lesson):
    if lesson in course_plan:
        index_of_lesson = course_plan.index(lesson)
        if not check_for_exercise(index_of_lesson):
            course_plan.insert(index_of_lesson + 1, f"{lesson}-Exercise")
    elif lesson not in course_plan:
        course_plan.append(lesson)
        course_plan.append(f"{lesson}-Exercise")


course_plan = input().split(', ')

command = input().split(':')
while command[0] != "course start":
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        add(lesson_title)
    elif action == "Insert":
        index = int(command[2])
        insert(lesson_title, index)
    elif action == "Remove":
        remove(lesson_title)
    elif action == "Swap":
        lessons_2 = command[2]
        swap(lesson_title, lessons_2)
    elif action == "Exercise":
        exercise(lesson_title)

    command = input().split(':')

# print(*(f"{x}.{i}" for x, i in enumerate(course_plan, 1)), sep="\n")
for pos, lesson in enumerate(course_plan, 1):
    print(f"{pos}.{lesson}")
