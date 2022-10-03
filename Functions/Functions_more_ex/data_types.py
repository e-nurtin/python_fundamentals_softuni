# def check_input_type(data):
#     read = ""
#     if data.isdigit():
#         read = int(data)
#         read *= 2
#     elif "." in data:
#         read = float(data)
#         read *= 1.5
#         read = "{:.2f}".format(read)
#     elif data.isalpha():
#         read = f"${data}$"
#     return read
#

def check_input_type(type, value):
    read = ""
    if type == "int":
        read = int(value)
        read *= 2
    elif type == "real":
        read = float(value)
        read *= 1.5
        read = "{:.2f}".format(read)
    elif type == "string":
        read = f"${value}$"
    return read


type_input = input()
value_input = input()

print(check_input_type(type_input, value_input))
