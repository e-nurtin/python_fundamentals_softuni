import re


def define_decrypt_value(pattern, message):
    decrypt_value = len(re.findall(pattern, message, re.I))
    return decrypt_value


def decrypt_msg(value_to_subtract, message):
    decrypted_message = ""
    for character in message:
        decrypted_message += chr(ord(character) - value_to_subtract)
    return decrypted_message


data = {"A": {}, "D": {}}
decrypted_messages = []

count_of_messages = int(input())

count_star_pattern = r"([star])"
decrypted_msg_pattern = r"@{1}([A-Za-z]+)[^-!:>@]*:(\d+)" \
                        r"[^-!:>@]*!([AD]{1})![^-!:>@]*->(\d+)"

for i in range(count_of_messages):
    encrypted_msg = input()

    value = define_decrypt_value(count_star_pattern, encrypted_msg)
    decrypted_messages.append(decrypt_msg(value, encrypted_msg))

for message in decrypted_messages:
    data_found = re.search(decrypted_msg_pattern, message)

    if data_found:
        name, population, attack, soldiers = data_found.groups()
        data[attack][name] = [population, soldiers]


print(f"Attacked planets: {len(data['A'])}")
for planet_name in sorted(data["A"].keys()):
    print(f"-> {planet_name}")
print(f"Destroyed planets: {len(data['D'])}")
for planet_name in sorted(data["D"].keys()):
    print(f"-> {planet_name}")
