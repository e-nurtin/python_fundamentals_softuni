company_data = {}
command = input()
while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in company_data:
        company_data[company] = []
    if employee_id not in company_data[company]:
        company_data[company].append(employee_id)
    command = input()
for company in company_data:
    print(company)
    for employee in company_data[company]:
        print(f"-- {employee}")