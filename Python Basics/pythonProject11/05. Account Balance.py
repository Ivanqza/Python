total = 0
command = input()
while command != "NoMoreMoney":
    current_amount = float(command)
    if current_amount < 0:
        print("Invalid operation!")
        break
    total += current_amount
    print(f"Increase: {current_amount:.2f}")
    command = input()
print(f"Total: {total:.2f}")