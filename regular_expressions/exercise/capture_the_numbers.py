import re

text = input()
result = []

while text != "":

    result.extend(re.findall(r"\d+", text))

    text = input()
print(' '.join(result))