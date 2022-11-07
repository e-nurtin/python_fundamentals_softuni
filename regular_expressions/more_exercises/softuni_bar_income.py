import re

pattern = r"\B[^%$\.\|]*%([A-Z]{1}[a-z]+)%[^%$\.\|]*<([\w]+)>" \
          r"[^%$\.\|]*\|([\d]+)\|[^%$\.\|]*([1-9]+[\.\d]*)\$\B"

text = input()
total_income = 0

while text != "end of shift":

    current_bill = 0
    result = re.search(pattern, text)

    if result:
        name, product, quantity, price = result.groups()
        current_bill = int(quantity) * float(price)
        total_income += current_bill
        print(f"{name}: {product} - {current_bill:.2f}")

    text = input()

print(f"Total income: {total_income:.2f}")