# print([round(float(el)) for el in input().split()])    - решение на 1 ред

nums = [float(el) for el in input().split()]
rounded = map(round, nums)
print(list(rounded))