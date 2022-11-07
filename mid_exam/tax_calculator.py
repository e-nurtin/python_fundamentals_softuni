vehicles_for_taxes = input().split(">>")

total_taxes_to_be_collected = 0


for vehicle in vehicles_for_taxes:
    car_is_valid = True
    taxes = 0
    current_vehicle_tax = 0
    discount = 0
    increase = 0

    vehicle_type, years_in_use, kilometers = [int(x) if x.isdigit() else x
                                              for x in vehicle.split()]

    if vehicle_type == "family":
        current_vehicle_tax = 50
        discount = years_in_use * 5
        increase = (kilometers // 3000) * 12
        taxes = current_vehicle_tax + increase - discount

    elif vehicle_type == "heavyDuty":
        current_vehicle_tax = 80
        discount = years_in_use * 8
        increase = (kilometers // 9000) * 14
        taxes = current_vehicle_tax + increase - discount

    elif vehicle_type == "sports":
        current_vehicle_tax = 100
        discount = years_in_use * 9
        increase = (kilometers // 2000) * 18
        taxes = current_vehicle_tax + increase - discount
    else:
        print("Invalid car type.")
        car_is_valid = False

    if car_is_valid:
        total_taxes_to_be_collected += taxes
        print(f"A {vehicle_type} car will pay {taxes:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect "
      f"{total_taxes_to_be_collected:.2f} euros in taxes.")
