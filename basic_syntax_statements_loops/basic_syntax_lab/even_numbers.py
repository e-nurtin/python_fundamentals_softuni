number_count = int(input())

for number in range(number_count):
    current_number = int(input())
    if current_number % 2 == 0:
        continue
    else:
        print(f"{current_number} is odd!")
        break
if current_number % 2 == 0:
    print("All numbers are even.")