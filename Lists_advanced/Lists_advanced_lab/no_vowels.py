user_input = input()
vowels = ['a', 'o', 'u', 'e', 'i']
without_vowels = [x for x in user_input if x.lower() not in vowels]
result = "".join(without_vowels)
print(result)