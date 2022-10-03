def check_indexes(guesses):
    if command[0] == command[1] or \
            int(command[0]) < 0 or \
            int(command[1]) < 0 or \
            len(sequence_to_guess) <= int(command[0]) or \
            len(sequence_to_guess) <= int(command[1]):
        print("Invalid input! Adding additional elements to the board")
        sequence_to_guess.insert((len(sequence_to_guess)//2), f"-{guesses}a")
        sequence_to_guess.insert((len(sequence_to_guess)//2), f"-{guesses}a")
    else:
        return True


def check_elements(guesses):
    element_1 = sequence_to_guess[int(command[0])]
    element_2 = sequence_to_guess[int(command[1])]
    if check_indexes(guesses):
        if element_1 == element_2:
            print(f"Congrats! You have found matching elements - "
                  f"{sequence_to_guess[int(command[0])]}!")
            for word in sequence_to_guess:
                if word == element_1:
                    sequence_to_guess.remove(word)
            if len(sequence_to_guess) == 0:
                check_for_win(guesses)
        else:
            print("Try again!")


def check_for_win(guesses):
    if len(sequence_to_guess) == 0:
        print(f"You have won in {guesses} turns!")
    else:
        print("Sorry you lose :(")
        print(" ".join(sequence_to_guess))
    exit()


number_of_guesses = 0
sequence_to_guess = input().split()
command = input().split()
while command[0] != "end":
    number_of_guesses += 1
    check_elements(number_of_guesses)
    command = input().split()
check_for_win(number_of_guesses)
