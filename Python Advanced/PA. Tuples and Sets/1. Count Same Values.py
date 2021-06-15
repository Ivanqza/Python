numbers = tuple([float(el) for el in input().split()])

counter_dict = {}

for num in numbers:
    if num not in counter_dict:
        counter_dict[num] = 0
    counter_dict[num] += 1

for key, value in counter_dict.items():
    print(f"{key} - {value} times")