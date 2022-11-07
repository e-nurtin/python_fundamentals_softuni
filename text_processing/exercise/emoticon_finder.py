text = input()

for index, symbol in enumerate(text):
    emoticon = ""
    if symbol == ":":
        emoticon = text[index:index + 2]
        print(emoticon)
