divisor = int(input())
boundary = int(input())
largest_divisible = 0
for number in range(divisor, boundary + 1):
    if number % divisor == 0:
        largest_divisible = number
print(largest_divisible)
