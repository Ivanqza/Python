n = int(input())

max_so_far = None
for _ in range(n):
    first, second = input().split('-')

    first = first.split(',')
    second = second.split(',')

    first = (int(first[0]), int(first[1]))
    second = (int(second[0]), int(second[1]))

    near = max(first[0], second[0])
    far = min(first[1], second[1])

    current_span = far - near + 1

    if max_so_far is None or current_span > len(max_so_far):
        max_so_far = list(range(near, far + 1))

print(f' Longest intersection is {max_so_far} with length {len(max_so_far)}')