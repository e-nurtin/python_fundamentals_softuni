divisor = int(input())
boundary_range = int(input())

largest_divisible_number = 0

for current_number in range(1, boundary_range + 1):
    if current_number % divisor == 0:
        largest_divisible_number = current_number

print(largest_divisible_number)