employee_capacity_1 = int(input())
employee_capacity_2 = int(input())
employee_capacity_3 = int(input())

students_count = int(input())

total_capacity_per_hour = employee_capacity_1 + employee_capacity_2 +\
                          employee_capacity_3
hours_needed = 0
while students_count > 0:
    hours_needed += 1
    if hours_needed % 4 == 0:
        continue
    students_count -= total_capacity_per_hour

print(f"Time needed: {hours_needed}h.")
