spell_to_decipher = input()


def case_replace(info, spell):
    if info == 'upper':
        for letter in spell:
            spell = spell.replace(letter, letter.upper())
    elif info == 'lower':
        for letter in spell:
            spell = spell.replace(letter, letter.lower())
    print(spell)
    return spell


def letter_replace(info, spell):
    index, letter = int(info[0]), info[1]
    if 0 <= index < len(spell):
        spell = spell[:index] + letter + spell[index + 1:]
        print('Done!')
    else:
        print("The spell was too weak.")
    return spell


def replace(substring, substitute, spell):
    return spell.replace(substring, substitute)


command = input()
while command != "Abracadabra":
    action, *info = command.split()

    if action == "Abjuration":
        spell_to_decipher = case_replace('upper', spell_to_decipher)
    elif action == "Necromancy":
        spell_to_decipher = case_replace('lower', spell_to_decipher)
    elif action == "Illusion":
        spell_to_decipher = letter_replace(info, spell_to_decipher)
    elif action == "Divination":
        substring, substitute = info[0], info[1]
        if substring in spell_to_decipher:
            spell_to_decipher = replace(substring, substitute, spell_to_decipher)
            print(spell_to_decipher)
    elif action == "Alteration":
        substring = info[0]
        if substring in spell_to_decipher:
            spell_to_decipher = replace(substring, '', spell_to_decipher)
            print(spell_to_decipher)

    else:
        print("The spell did not work!")

    command = input()
