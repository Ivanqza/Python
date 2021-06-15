def create_matrix(row_size, col_size):
    matrix = []
    for _ in range(row_size):
        matrix.append([])
        for _ in range(col_size):
            matrix[-1].append('')

    return matrix


n, m = input().split()
n, m = int(n), int(m)
text = input()

matrix = create_matrix(n, m)

text_index = 0
col = 0

for row in range(n):
    if row % 2 == 0:
        dir = 1
    else:
        dir = -1

    while 0 <= col < m:
        matrix[row][col] = text[text_index]
        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += dir
    col -= dir

for i in range(len(matrix)):
    print(''.join(matrix[i]))

# from collections import deque
#
# rows, cols = map(int, input().split())
# snake = deque(input())
# mx = []
#
# for y in range(rows):
#     for x in range(cols):
#         snake.append(snake.popleft())
#         if y % 2 == 0:
#             mx.append(snake[-1])
#         else:
#             mx.insert(0, snake[-1])
#     print(''.join(mx))
#     mx = []