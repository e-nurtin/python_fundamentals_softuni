import re

count_of_products = int(input())
barcode_pattern = r"(?:@#{1,})(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])(?:@#{1,})"

for _ in range(count_of_products):
    current_barcode = input()
    match = re.match(barcode_pattern, current_barcode)

    if match:
        product_group = '00'
        product = match.group('product')
        digits = re.findall("\d", product)

        if digits:
            product_group = ''.join(digits)
        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
