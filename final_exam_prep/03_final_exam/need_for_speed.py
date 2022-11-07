def drive_car(model, distance, needed_fuel, fuel_d, kilometers_d):
    if data[model][fuel_d] < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        data[model][fuel_d] -= needed_fuel
        data[model][kilometers_d] += distance
        print(f"{model} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if data[model][kilometers_d] >= 100_000:
            print(f"Time to sell the {model}!")
            del data[model]


def refuel_car(model, refill_amount, fuel_d):
    max_amount = 75
    if data[model][fuel_d] + refill_amount > max_amount:
        refill_amount = max_amount - data[model][fuel_d]
    data[model][fuel_d] += refill_amount
    print(f"{model} refueled with {refill_amount} liters")


def revert_kms(model, kilometers, km_d):
    data[model][km_d] -= kilometers
    if data[model][km_d] < 10_000:
        data[model][km_d] = 10_000
    else:
        print(f"{model} mileage decreased by {kilometers} kilometers")

data = {}
km_d = 'kilometers'
fuel_d = 'fuel'

number_of_cars = int(input())

for i in range(number_of_cars):
    car, mileage, fuel_available = [int(x) if x.isdigit() else x for x in input().split("|")]
    data[car] = {}
    data[car][km_d] = mileage
    data[car][fuel_d] = fuel_available

command = input()

while command != "Stop":
    action, car, *info = [int(x) if x.isdigit() else x for x in command.split(" : ")]

    if action == "Drive":
        drive_car(car, info[0], info[1], fuel_d, km_d)
    elif action == "Refuel":
        refuel_car(car, info[0], fuel_d)
    elif action == "Revert":
        revert_kms(car, info[0], km_d)
    command = input()

for model, info in data.items():
    print(f"{model} -> Mileage: {info[km_d]} kms, Fuel in the tank: {info[fuel_d]} lt.")