count_of_iterations = int(input())

positive_numbers = []
negative_numbers = []
count_positive_numbers = 0
sum_of_negatives = 0
for i in range(count_of_iterations):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)
        count_positive_numbers += 1
    elif current_number < 0:
        negative_numbers.append(current_number)
        sum_of_negatives += current_number

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}\n"
      f"Sum of negatives: {sum(negative_numbers)}")