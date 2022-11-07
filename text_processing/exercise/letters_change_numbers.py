strings = input().split()
total_sum = 0
for string in strings:

    digits = [i for i in string if i.isdigit()]
    number = int(''.join(digits))

    first_letter = string[0]
    last_letter = string[-1]

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    elif first_letter.islower():
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    elif last_letter.islower():
        number += (ord(last_letter) - 96)

    total_sum += number

print(f"{total_sum:.2f}")
