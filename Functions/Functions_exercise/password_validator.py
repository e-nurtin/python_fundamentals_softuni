# def password_validator(password):
#     digit_counter = 0
#     test_pass = 0
#     if 6 <= len(password) <= 10:
#         test_pass += 1
#     else:
#         return print("Password must be between 6 and 10 characters")
#     if password.isalnum():
#         test_pass += 1
#     else:
#         print("Password must consist only of letters and digits")
#     for digit in password:
#         if digit.isdigit():
#             digit_counter += 1
#             if digit_counter == 2:
#                 test_pass += 1
#     if digit_counter < 2:
#         print("Password must have at least 2 digits")
#     if test_pass == 3:
#         return print("Password is valid")
#     return False


def password_length(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def password_characters(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def password_digits(password):
    digit_counter = 0
    for digit in password:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


input_password = input()
validation = [password_length(input_password),
              password_characters(input_password),
              password_digits(input_password)]
if all(validation):
    print("Password is valid")