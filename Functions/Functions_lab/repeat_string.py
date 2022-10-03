# function_repeat = lambda string, count: string * count

def repeat(string: str, count: int):
    return string * count


original_string = input()
count_of_repeats = int(input())

print(repeat(original_string, count_of_repeats))