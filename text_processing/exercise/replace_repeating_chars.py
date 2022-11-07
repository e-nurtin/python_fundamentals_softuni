string = input()
last_letter = ""
new_string = ""
for letter in string:
    if last_letter != letter:
        new_string += letter
        last_letter = letter
print(new_string)