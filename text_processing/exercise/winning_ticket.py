def check_for_win(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    for symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            if repetition * symbol in left_half and repetition * symbol in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = input().split(', ')
count_first = 0
count_second = 0
winning_symbols = ['@', '#', '$', '^']
for element in tickets:
    ticket = element.strip()
    print(check_for_win(ticket))
