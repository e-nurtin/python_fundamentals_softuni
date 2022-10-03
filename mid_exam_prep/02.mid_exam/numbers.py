numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)
greater_than_average = [x for x in numbers if x > average]
greater_than_average.sort(reverse=True)

if len(greater_than_average) == 0:
    print("No")
else:
    print(*greater_than_average[:5], sep=' ')