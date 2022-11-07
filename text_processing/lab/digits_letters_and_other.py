string = input()
print(''.join([x for x in string if x.isdigit()]))
print(''.join([x for x in string if x.isalpha()]))
print(''.join([x for x in string if not x.isalpha() and not
               x.isdigit()]))
