def multiplication(num_1, num_2, num_3):
    if (num_1 > 0 and num_2 < 0 and num_3 < 0) or \
            (num_2 > 0 and num_1 < 0 and num_3 < 0) or \
            (num_3 > 0 and num_1 < 0 and num_2 < 0) or \
            (num_1 > 0 and num_2 > 0 and num_3 > 0):
        return "positive"
    elif num_1 == 0 or num_2 == 0 or num_3 == 0:
        return "zero"
    elif num_1 < 0 or num_2 < 0 or num_3 < 0:
        return "negative"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(multiplication(number_1, number_2, number_3))
