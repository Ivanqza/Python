n = int(input())

names = set()

for x in range(n):
    names.add(input())

[print(name) for name in names]