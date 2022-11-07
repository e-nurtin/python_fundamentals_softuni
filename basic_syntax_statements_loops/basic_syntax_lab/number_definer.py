number = float(input())

if 0.0 < abs(number) < 1.0:
    print("small", end=' ')
elif abs(number) > 1_000_000:
    print("large", end=' ')
if number == 0:
    print("zero")
elif number > 0:
    print("positive")
elif number < 0:
    print("negative")
