def tribonacci(number):
    sequence = [1]
    for n in range(1, number):
        if n == 1:
            sequence.append(1)
        elif n == 2:
            sequence.append(2)
        else:
            sequence.append(sequence[n - 1] + sequence[n - 2] + sequence[n - 3])
    return sequence


num = int(input())
list_tribonacci = tribonacci(num)

for item in list_tribonacci:
    print(item, end=" ")