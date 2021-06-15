def read_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append([])
        for elem in input().split():
            inner_list = matrix[-1]
            inner_list.append(int(elem))

    return matrix

n = int(input())
matrix = read_matrix(n)

main_diagonal = 0
secondary_diagonal = 0
for i in range(n):
    main_diagonal += matrix[i][i]
for i in range(n):
    secondary_diagonal += matrix[len(matrix) - 1 - i][i]

print(abs(main_diagonal - secondary_diagonal))