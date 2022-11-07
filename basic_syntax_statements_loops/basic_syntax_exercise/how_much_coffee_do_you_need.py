# current_command = input()
# coffee_count = 0
# while current_command != "END":
#     if current_command == "coding":
#         coffee_count += 1
#     elif current_command == "CODING":
#         coffee_count += 2
#     elif current_command == "cat" or current_command == "dog":
#         coffee_count += 1
#     elif current_command == "CAT" or current_command == "DOG":
#         coffee_count += 2
#     elif current_command == "movie":
#         coffee_count += 1
#     elif current_command == "MOVIE":
#         coffee_count += 2
#
#     current_command = input()
# if coffee_count > 5:
#     print("You need extra sleep")
# else:
#     print(coffee_count)

current_command = input()
need_coffee_for = ['coding', 'movie', 'dog', 'cat']
coffee_count = 0
while current_command != 'END':
    if current_command.lower() in need_coffee_for:
        if current_command.isupper():
            coffee_count += 2
        else:
            coffee_count += 1

    current_command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
