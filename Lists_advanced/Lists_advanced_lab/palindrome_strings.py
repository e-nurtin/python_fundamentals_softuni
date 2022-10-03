def palindrome_check(list_of_input):
    return [x for x in list_of_input if x[::-1] == x]


user_input = input().split()
palindrome_word = input()
palindrome_words = palindrome_check(user_input)
print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(palindrome_word)} times")