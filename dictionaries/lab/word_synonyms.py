count_of_words_to_read = int(input())
synonym_dictionary = {}

for i in range(count_of_words_to_read):
    word = input()
    if word not in synonym_dictionary:
        synonym_dictionary[word] = []
    synonym = input()
    synonym_dictionary[word].append(synonym)

for key, value in synonym_dictionary.items():
    print(f"{key} - {', '.join(value)}")
