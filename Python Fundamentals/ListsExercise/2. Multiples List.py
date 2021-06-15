factor = int(input())
count = int(input())

list = []

for index in range(factor, factor * count + 1, factor):
    list.append(index)

print(list)