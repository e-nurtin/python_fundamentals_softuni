import math

people_to_elevate = int(input())
elevator_capacity = int(input())
courses = 0
if elevator_capacity != 0:
    courses = math.ceil(people_to_elevate / elevator_capacity)
print(courses)