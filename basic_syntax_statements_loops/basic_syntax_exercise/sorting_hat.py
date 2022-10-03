current_name = input()
while current_name != "Welcome!":
    length_of_name = len(current_name)

    if current_name == "Voldemort":
        print("You must not speak of that name!")
        break
    if length_of_name < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif length_of_name == 5:
        print(f"{current_name} goes to Slytherin.")
    elif length_of_name == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif length_of_name > 6:
        print(f"{current_name} goes to Hufflepuff.")

    current_name = input()

if current_name == "Welcome!":
    print("Welcome to Hogwarts.")