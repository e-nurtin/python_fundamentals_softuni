random_word = input()
word_case_insensitive = random_word.lower()
sun_word_count = word_case_insensitive.count("sun")
water_word_count = word_case_insensitive.count("water")
sand_word_count = word_case_insensitive.count("sand")
fish_word_count = word_case_insensitive.count("fish")
total_word_count = sun_word_count + water_word_count + sand_word_count + fish_word_count
print(total_word_count)