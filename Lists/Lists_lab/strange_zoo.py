tail = input()
body = input()
head = input()
#
# ordered_animal = [head, body, tail]
animal = [tail, body, head]
animal[0], animal[2] = animal[2], animal[0]
print(animal)