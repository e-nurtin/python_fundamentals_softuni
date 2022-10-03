# # 1
# print(list(map(lambda a: round(float(a)), input().split())))
#
# # 2
#
# def round_numbers(numbers: str):
#     float_list = list(map(float, numbers.split()))
#     rounded_list = list(map(round, float_list))
#     return rounded_list
#
#
# original_input = input()
# print(round_numbers(original_input))
#
# # 3

def round_function(sentence: str):
    sentence = sentence.split()
    rounded_numbers = []

    for number in sentence:
        number = round(float(number))
        rounded_numbers.append(number)

    return print(rounded_numbers)


original_input = input()
round_function(original_input)

