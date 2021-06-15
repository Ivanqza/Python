n = int(input())
heroes = {}
amount_recharged = 0
for n in range(n):
    hero_name, health, mana = input().split(" ")
    health = int(health)
    mana = int(mana)
    heroes[hero_name] = {'health': health, 'mana': mana}

data = input()

while not data == "End":
    if data.startswith("CastSpell"):
        data, hero_name, mana_needed, spell_name = data.split(" - ")
        mana_needed = int(mana_needed)
        if mana_needed <= heroes[hero_name]['mana']:
            heroes[hero_name]['mana'] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif data.startswith("TakeDamage"):
        data, hero_name, damage, attacker = data.split(" - ")
        damage = int(damage)
        if damage < heroes[hero_name]['health']:
            heroes[hero_name]['health'] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['health']} HP left!")
        else:
            heroes[hero_name]['health'] -= damage
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
    elif data.startswith("Recharge"):
        data, hero_name, amount = data.split(" - ")
        amount = int(amount)
        amount_recharged = 200 - heroes[hero_name]['mana']
        heroes[hero_name]['mana'] += amount
        if heroes[hero_name]['mana'] > 200:
            heroes[hero_name]['mana'] = 200
            print(f"{hero_name} recharged for {amount_recharged} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif data.startswith("Heal"):
        data, hero_name, amount = data.split(" - ")
        amount = int(amount)
        amount_recharged = 100 - heroes[hero_name]['health']
        heroes[hero_name]['health'] += amount
        if heroes[hero_name]['health'] > 100:
            heroes[hero_name]['health'] = 100
            print(f"{hero_name} healed for {amount_recharged} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
    data = input()

sorted_heroes = sorted(heroes.items(), key=lambda tkvp: (-tkvp[1]['health'], tkvp[0]))

for hero, values in sorted_heroes:
    print(hero)
    print(f"  HP: {values['health']}\n  MP: {values['mana']}")