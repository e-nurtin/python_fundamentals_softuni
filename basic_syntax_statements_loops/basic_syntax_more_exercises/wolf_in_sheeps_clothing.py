animals = input()
animal_list = list(animals.split(", "))
sheep_counter = 0

for index, current_animal in enumerate(reversed(animal_list)):
    if current_animal == "wolf" and index == 0:
        print("Please go away and stop eating my sheep")
        break
    if current_animal == "wolf":
        print(f"Oi! Sheep number {sheep_counter}!"
              f" You are about to be eaten by a wolf!")
        break
    sheep_counter += 1
        