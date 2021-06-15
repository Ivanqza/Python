def change_element(row, col):
    base = ord('a')
    first = chr(row + base)
    second = chr(row + col + base)
    return f'{first}{second}{first}'


n, m = input().split()
n, m = int(n), int(m)
matrix = [[change_element(row, col) for col in range(m)]for row in range(n)]

# разширено разписване без функция и комприхеншън
# matrix = []
# base = ord('a')
# for row in range(n):
#     matrix.append([])
#     for col in range(m):
#         first = chr(row + base)
#         second = chr(row + col + base)
#         matrix[-1].append(f'{first}{second}{first}')


print('\n'.join(' '.join([str(el) for el in row])for row in matrix))