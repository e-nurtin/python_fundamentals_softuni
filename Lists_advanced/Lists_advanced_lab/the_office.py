employee_happiness_list = list(map(int, input().split()))
happiness_factor = int(input())

employees = [x * happiness_factor for x in employee_happiness_list]
avg_happiness = sum(employees) // len(employee_happiness_list)
happy_people = list(filter(lambda x: x > avg_happiness, employees))

if len(employees) / 2 > len(happy_people):
    print(f"Score: {len(happy_people)}/{len(employees)}. Employees are not "
          f"happy!")
else:
    print(f"Score: {len(happy_people)}/{len(employees)}. Employees are happy!")
