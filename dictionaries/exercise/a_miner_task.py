resources_dictionary = {}
resource = input()
while resource != "stop":
    quantity = int(input())
    if resource not in resources_dictionary:
        resources_dictionary[resource] = 0
    resources_dictionary[resource] += quantity

    resource = input()

for key, value in resources_dictionary.items():
    print(f"{key} -> {value}")