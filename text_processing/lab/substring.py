string_to_remove = input()
from_string = input()

while string_to_remove in from_string:
    from_string = from_string.replace(string_to_remove, "")
    # start = from_string.find(string_to_remove)
    # end = start + len(string_to_remove)
    # from_string = from_string[:start] + from_string[end:]
print(from_string)
