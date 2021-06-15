number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {'mileage': mileage, 'fuel': fuel}

data = input()

while not data == "Stop":
    command = data.split(" : ")
    if command[0] == "Drive":
        car, distance, fuel = command[1:]
        distance = int(distance)
        fuel = int(fuel)
        if fuel > cars[car]['fuel']:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] > 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car, fuel = command[1:]
        fuel = int(fuel)
        diff = 75 - cars[car]['fuel']
        cars[car]['fuel'] += fuel
        if cars[car]['fuel'] > 75:
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {diff} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car, kilometers = command[1:]
        kilometers = int(kilometers)
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]['mileage'] = 10000
    data = input()

sorted_cars = sorted(cars.items(), key=lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))
for car, values in sorted_cars:
    print(f"{car} -> Mileage: {values['mileage']} kms, Fuel in the tank: {values['fuel']} lt.")