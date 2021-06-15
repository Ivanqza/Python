import re

order = input()
pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
furniture_names = []
total_money = 0

while not order == "Purchase":
    match = re.match(pattern, order)
    if match:
        data = match.groupdict()
        furniture_names.append(data["name"])
        total_money += int(data["quantity"]) * float(data["price"])
    order = input()

print(f"Bought furniture:")
if furniture_names:
    print("\n".join(furniture_names))
print(f"Total money spend: {total_money:.2f}")
