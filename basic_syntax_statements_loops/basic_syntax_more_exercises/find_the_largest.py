number = int(input())
number_as_string = str(number)
for n in sorted(number_as_string, reverse=True):
    print(n, end="")