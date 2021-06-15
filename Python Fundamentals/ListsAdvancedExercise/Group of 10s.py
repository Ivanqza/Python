numbers = [int(el) for el in input().split(", ")]
# numbers = list(map(lambda x: int(x), input().split(", ")))
# numbers = list(map(int, input().split(", ")))
max_number = max(numbers)
num_of_groups = max_number // 10
group = 10


while numbers:
    nums_group = []

    for num in numbers:
        if num in range(group-10, group+1):
            nums_group.append(num)

    for num in nums_group:
        numbers.remove(num)

    print(f"Group of {group}'s: {nums_group}")
    group += 10