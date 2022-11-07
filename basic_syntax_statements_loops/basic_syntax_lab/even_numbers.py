#
#
# count_of_numbers = int(input())
# numbers_are_even = True
# for i in range(count_of_numbers):
#     number = int(input())
#     if number % 2 != 0:
#         print(f"{number} is odd!")
#         numbers_are_even = False
#         break
# if numbers_are_even:
#     print("All numbers are even.")


count_of_numbers = int(input())

for i in range(count_of_numbers):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
