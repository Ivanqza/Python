heroes = input().split(', ')
inventory = {hero: {} for hero in heroes}
line = input()
while line != 'End':
    hero, item_name, item_cost = line.split('-')

    if item_name not in inventory[hero]:
        inventory[hero][item_name] = int(item_cost)

    line = input()


# разширено изписване на принта
# for hero in heroes:
#     total_cost = sum(inventory[hero].values())
#     item_count = len(inventory[hero])
#     print(f'{hero} -> Items: {item_count}, Cost: {total_cost}')

print('\n'.join(f'{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}' for hero in heroes))