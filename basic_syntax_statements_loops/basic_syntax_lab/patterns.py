number_count = int(input())

for i in range(1, number_count + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(number_count -1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()