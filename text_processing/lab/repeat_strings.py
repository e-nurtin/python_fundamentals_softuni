# list_of_strings = input().split()
# result = [x*len(x) for x in list_of_strings]
# print(''.join(result))


# for string in list_of_strings:
#     string *= len(string)
#     result += string
# print(result)

# def repeat_string(string):
#     return string * len(string)
#
#
# list_of_strings = input().split()
# print(''.join(map(repeat_string, list_of_strings)))


class StringRepeat:
    def __init__(self, list_of_string):
        self.list_of_string = list_of_string

    def ret(self):
        result = ""
        for i in range(len(self.list_of_string)):
            string = list_of_strings[i]
            result += string * len(string)
        return result


list_of_strings = input().split()
return_string = StringRepeat(list_of_strings)
print(return_string.ret())