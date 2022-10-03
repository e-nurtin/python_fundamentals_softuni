number_of_orders = int(input())

total_price_of_all_orders = 0

for n in range(number_of_orders):
    price_per_capsule = float(input())
    days_of_orders = int(input())
    capsules_per_day = int(input())
    current_order_price = 0

    if 0.01 <= price_per_capsule <= 100:
        if 0 < days_of_orders <= 31:
            if 0 < capsules_per_day <= 2000:
                current_order_price = (days_of_orders * capsules_per_day) \
                                      * price_per_capsule
                total_price_of_all_orders += current_order_price

                print(
                    f"The price for the coffee is: ${current_order_price:.2f}")

print(f"Total: ${total_price_of_all_orders:.2f}")
