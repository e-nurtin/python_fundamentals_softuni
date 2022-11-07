def add_piece(piece, composer, key):
    if piece not in data:
        data[piece] = [composer, key]
        return f"{piece} by {composer} in {key} added to the collection!"
    else:
        return f"{piece} is already in the collection!"


def remove_piece(piece):
    if piece in data:
        del data[piece]
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change_key(piece, new_key):
    if piece in data:
        data[piece][1] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


data = {}
count_of_pieces = int(input())

for i in range(count_of_pieces):
    piece, composer, key = input().split('|')
    data[piece] = [composer, key]


command = input()
while command != "Stop":
    action, *info = command.split('|')

    if action == "Add":
        print(add_piece(info[0], info[1], info[2]))
    elif action == "Remove":
        print(remove_piece(info[0]))
    elif action == "ChangeKey":
        print(change_key(info[0], info[1]))

    command = input()

for piece, composer in data.items():
    print(f"{piece} -> Composer: {composer[0]}, Key: {composer[1]}")