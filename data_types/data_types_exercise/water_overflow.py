count_of_numbers = int(input())
water_tank_capacity = 255
total_filled = 0
for i in range(count_of_numbers):
    current_pour = int(input())
    if water_tank_capacity - current_pour < 0:
        print("Insufficient capacity!")
        continue
    total_filled += current_pour
    water_tank_capacity -= current_pour
print(total_filled)
