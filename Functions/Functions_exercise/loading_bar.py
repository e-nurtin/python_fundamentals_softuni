def loading_bar(number: int):
    bar = "[..........]"
    percent = int(number / 10)
    new_string = bar.replace(".", "%", percent)
    if number != 100:
        return f"{number}% {new_string}\nStill loading..."
    return f"{number}% Complete!\n{new_string}"


initial_number = int(input())

print(loading_bar(initial_number))
