def correct_exercise_placement(lesson_to_add, lesson):
    lesson_schedule.remove(lesson_to_add)
    index = lesson_schedule.index(lesson)
    lesson_schedule.insert(index + 1, lesson_to_add)


def add_lesson(lesson):
    if lesson not in lesson_schedule:
        lesson_schedule.append(lesson)


def insert_lesson(lesson, index):
    if lesson not in lesson_schedule:
        if 0 <= index <= len(lesson):
            lesson_schedule.insert(index, lesson)


def remove_lesson(lesson):
    lesson_exercise = lesson + '-Exercise'
    if lesson in lesson_schedule:
        lesson_schedule.remove(lesson)
    if lesson_exercise in lesson_schedule:
        lesson_schedule.remove(lesson_exercise)


def swap_lessons(lesson_one, lesson_two):
    lesson_one_exercise = lesson_one + '-Exercise'
    lesson_two_exercise = lesson_two + '-Exercise'

    if lesson_one and lesson_two in lesson_schedule:
        index_l_one = lesson_schedule.index(lesson_one)
        index_l_two = lesson_schedule.index(lesson_two)

        lesson_schedule[index_l_one], lesson_schedule[index_l_two] = \
            lesson_schedule[index_l_two], lesson_schedule[index_l_one]

        if lesson_one_exercise in lesson_schedule:
            correct_exercise_placement(lesson_one_exercise, lesson_one)

        if lesson_two_exercise in lesson_schedule:
            correct_exercise_placement(lesson_two_exercise, lesson_two)


def add_exercise(lesson):
    lesson_exercise = lesson + '-Exercise'
    if lesson not in lesson_schedule:
        lesson_schedule.append(lesson)
    if lesson_exercise not in lesson_schedule:
        lesson_schedule.insert(lesson_schedule.index(lesson) + 1, lesson_exercise)


lesson_schedule = input().split(', ')

command = input()
while command != "course start":
    action, lesson_to_modify, *info = [x if x.isalpha() else int(x) for x in
                                       command.split(':')]

    if action == "Add":
        add_lesson(lesson_to_modify)
    elif action == "Insert":
        insert_lesson(lesson_to_modify, info[0])
    elif action == "Remove":
        remove_lesson(lesson_to_modify)
    elif action == "Swap":
        swap_lessons(lesson_to_modify, info[0])
    elif action == "Exercise":
        add_exercise(lesson_to_modify)

    command = input()

for pos, current_lesson in enumerate(lesson_schedule, 1):
    print(f"{pos}.{current_lesson}")



# def add(lesson):
#     if lesson not in course_plan:
#         course_plan.append(lesson)
#
#
# def insert(lesson, index_to_insert):
#     if lesson not in course_plan:
#         course_plan.insert(index_to_insert, lesson)
#
#
# def remove(lesson):
#     if lesson in course_plan:
#         index_of_lesson = course_plan.index(lesson)
#         del course_plan[index_of_lesson]
#         if check_for_exercise(index_of_lesson):
#             del course_plan[index_of_lesson]
#
#
# def swap(lesson_1, lesson_2):
#     if lesson_1 in course_plan and lesson_2 in course_plan:
#         index_1 = course_plan.index(lesson_1)
#         index_2 = course_plan.index(lesson_2)
#         course_plan[index_1], course_plan[index_2] = course_plan[index_2], \
#                                                      course_plan[index_1]
#         if check_for_exercise(index_1):
#             course_plan.insert(index_2 + 1, course_plan.pop(index_1 + 1))
#         if check_for_exercise(index_2):
#             course_plan.insert(index_1 + 1, course_plan.pop(index_2 + 1))
#
#
# def check_for_exercise(index_1):
#     try:
#         if 'Exercise' in course_plan[index_1 + 1]:
#             return True
#     except IndexError:
#         return False
#
#
# def exercise(lesson):
#     if lesson in course_plan:
#         index_of_lesson = course_plan.index(lesson)
#         if not check_for_exercise(index_of_lesson):
#             course_plan.insert(index_of_lesson + 1, f"{lesson}-Exercise")
#     elif lesson not in course_plan:
#         course_plan.append(lesson)
#         course_plan.append(f"{lesson}-Exercise")
#
#
# course_plan = input().split(', ')
#
# command = input().split(':')
# while command[0] != "course start":
#     action = command[0]
#     lesson_title = command[1]
#     if action == "Add":
#         add(lesson_title)
#     elif action == "Insert":
#         index = int(command[2])
#         insert(lesson_title, index)
#     elif action == "Remove":
#         remove(lesson_title)
#     elif action == "Swap":
#         lessons_2 = command[2]
#         swap(lesson_title, lessons_2)
#     elif action == "Exercise":
#         exercise(lesson_title)
#
#     command = input().split(':')
#
# # print(*(f"{x}.{i}" for x, i in enumerate(course_plan, 1)), sep="\n")
# for pos, lesson in enumerate(course_plan, 1):
#     print(f"{pos}.{lesson}")
