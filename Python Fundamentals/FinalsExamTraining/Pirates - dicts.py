command = input()
towns_dict = {}

while not command == "Sail":
    town, population, treasure = command.split("||")
    population = int(population)
    treasure = int(treasure)
    if town not in towns_dict:
        towns_dict[town] = [population, treasure]
    else:
        people, gold = towns_dict[town]
        people += population
        gold += treasure
        towns_dict[town] = [people, gold]

    command = input()

orders = input()

while not orders == "End":
    splitted_orders = orders.split("=>")
    if splitted_orders[0] == "Plunder":
        town = splitted_orders[1]
        people_killed = int(splitted_orders[2])
        looted_gold = int(splitted_orders[3])
        if town in towns_dict:
            populations, golds = towns_dict[town]
            populations -= people_killed
            golds -= looted_gold
            print(f"{town} plundered! {looted_gold} gold stolen, {people_killed} citizens killed.")
            if populations <= 0 or golds <= 0:
                towns_dict.pop(town)
                print(f"{town} has been wiped off the map!")
            else:
                towns_dict[town] = [populations, golds]
    if splitted_orders[0] == "Prosper":
        town = splitted_orders[1]
        added_gold = int(splitted_orders[2])
        if added_gold > 0:
            populations, gold = towns_dict[town]
            gold += added_gold
            towns_dict[town] = [populations, gold]
            print(f"{added_gold} gold added to the city treasury. {town} now has {gold} gold.")
        else:
            print(f"Gold added cannot be a negative number")
    orders = input()

print(f"Ahoy, Captain! There are {len(towns_dict)} wealthy settlements to go to:")
sorted_towns_dict = dict(sorted(towns_dict.items(), key=lambda kvp: (-kvp[1][1], kvp[0])))
for key, value in sorted_towns_dict.items():
    print(f"{key} -> Population: {sorted_towns_dict[key][0]} citizens, Gold: {sorted_towns_dict[key][1]} kg")