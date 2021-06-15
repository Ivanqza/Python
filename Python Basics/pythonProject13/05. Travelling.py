while True:
    destination = input()
    if destination == "End":
        break

    min_budget = float(input())

    saved_money = 0

    while saved_money < min_budget:
        current_money = float(input())
        saved_money += current_money

    print(f"Going to {destination}!")