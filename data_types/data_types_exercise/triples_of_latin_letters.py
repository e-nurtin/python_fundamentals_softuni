number_of_characters = int(input())
starting_symbol = 97
finishing_symbol = 97 + number_of_characters

for first_symbol in range(starting_symbol, finishing_symbol):
    for second_symbol in range(starting_symbol, finishing_symbol):
        for third_symbol in range(starting_symbol, finishing_symbol):
            print(chr(first_symbol), end="")
            print(chr(second_symbol), end="")
            print(chr(third_symbol))
