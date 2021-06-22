def is_even(num):
    return num % 2 == 0


numbers = [int(word) for word in input().split()]
print(list(filter(is_even, numbers)))
