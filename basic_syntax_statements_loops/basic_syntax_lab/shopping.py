budget = int(input())
max_budget = budget
current_spending = input()
while current_spending != "End":
    max_budget -= int(current_spending)
    if max_budget < 0:
        print("You went in overdraft!")
        break
    current_spending = input()
if max_budget >= 0:
    print("You bought everything needed.")