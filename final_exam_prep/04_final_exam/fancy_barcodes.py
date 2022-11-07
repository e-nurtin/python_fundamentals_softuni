import re

validity_pattern = re.compile(r"^@#{1,}([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})@#{1,}$")
digits_pattern = re.compile(r"[0-9]")

count_of_barcodes = int(input())

for i in range(count_of_barcodes):
    current_barcode = input()
    result = re.findall(validity_pattern, current_barcode)

    if result:
        group = "00"
        digits = re.findall(digits_pattern, result[0])
        if digits:
            group = ''.join(digits)
        print(f"Product group: {group}")

    else:
        print("Invalid barcode")
