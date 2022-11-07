def find_age_name(words):
    name = ""
    age = 0
    for word in words:
        if "@" in word and "|" in word:
            start = word.index("@") + 1
            end = word.index("|")
            name = word[start:end]
        if "#" in word and "*" in word:
            start = word.index("#") + 1
            end = word.index("*")
            age = int(word[start:end])
    return f"{name} is {age} years old."


count_of_lines = int(input())

for i in range(count_of_lines):

    sentence = input().split()

    print(find_age_name(sentence))
