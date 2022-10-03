total_hardware_price = 0
while True:
    command = input()
    if command == "regular" or command == "special":
        break
    price_of_current_hardware = float(command)
    if price_of_current_hardware < 0:
        print("Invalid price!")
        continue
    total_hardware_price += price_of_current_hardware
if total_hardware_price == 0:
    print("Invalid order!")
else:
    taxes = total_hardware_price * 0.20
    total_hardware_price_with_taxes = total_hardware_price + taxes
    if command == "special":
        total_hardware_price_with_taxes *= 0.90
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_hardware_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_hardware_price_with_taxes:.2f}$")
