list1 = input().split()
list2 = []
for x in list1:
    x = int(x)
    x = x * (-1)
    list2.append(x)
print(list2)