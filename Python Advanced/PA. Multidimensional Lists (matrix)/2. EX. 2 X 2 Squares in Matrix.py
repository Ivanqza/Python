def read_matrix(rows):
    matrix = []

    for _ in range(rows):
        letters = input().split(' ')
        matrix.append(letters)

    return matrix


rows, cols = [int(el) for el in input().split()]
matrix = read_matrix(rows)
counter = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            counter += 1

print(counter)