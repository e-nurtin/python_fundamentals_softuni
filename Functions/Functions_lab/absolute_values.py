

def absolute_numbers(number):
    result = [abs(numb) for numb in number]
    return result

numbers = list(map(float, input().split()))
print(absolute_numbers(numbers))