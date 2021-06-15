string = input().split('>')
result = []
explosions = 0
for index in string:
    if index[0].isdigit():
        explosions += int(index[0])
        if len(index) <= explosions:
            explosions -= len(index)
            index = '>'
        else:
            index = '>'+''.join(list(index[explosions::]))
            explosions = 0
    result.append(index)
print(*result, sep='')