fires_with_cells_list = input().split("#")
water_available = int(input())
total_fire_extinguished = 0
total_effort_spent = 0
cells_extinguished = []

for current_fire in fires_with_cells_list:
    for element in current_fire.split():
        if element.isdigit():
            value_of_cell = int(element)
    cell_is_valid = False
    if water_available >= value_of_cell:
        if "High" in current_fire:
            if 80 < value_of_cell < 126:
                cell_is_valid = True
        elif "Medium" in current_fire:
            if 50 < value_of_cell < 81:
                cell_is_valid = True
        elif "Low" in current_fire:
            if 0 < value_of_cell < 51:
                cell_is_valid = True
        if cell_is_valid:
            water_available -= value_of_cell
            cells_extinguished.append(value_of_cell)
            total_fire_extinguished += value_of_cell
            total_effort_spent += (value_of_cell * 0.25)

print("Cells:")
for cell in cells_extinguished:
    print(f"- {cell}")
print(f"Effort: {total_effort_spent:.2f}")
print(f"Total Fire: {total_fire_extinguished}")