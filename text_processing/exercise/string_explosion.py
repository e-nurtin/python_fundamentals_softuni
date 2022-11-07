text = input()
explosion_index = 0
strength_of_explosion = 0

for index, symbol in enumerate(text):

    if symbol == ">":
        explosion_index = index
        if text[explosion_index + 1].isdigit():
            strength_of_explosion += int(text[index + 1])

        while strength_of_explosion > 0:
            explosion_index += 1
            symbol = text[explosion_index]
            if symbol == ">":
                break
            if explosion_index + 1 >= len(text):
                text = text[:-1]
                break
            strength_of_explosion -= 1
            text = text[:explosion_index] + '!' + text[explosion_index + 1:]


text = text.replace('!', '')
print(text)

