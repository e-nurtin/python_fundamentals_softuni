def calculation(operation,first,second):
    result = None
    if operation == "multiply":
        result = first * second
    elif operation == "divide":
        result = first // second
    elif operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    return result


command = input()
number_one = int(input())
number_two = int(input())

print(calculation(command,number_one,number_two))