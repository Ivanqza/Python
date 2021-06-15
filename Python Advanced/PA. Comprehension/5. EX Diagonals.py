n = int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]
main_diag = ([matrix[i][i] for i in range(n)])
second_diag = ([matrix[i][n-1-i] for i in range(n)])
print(f'First diagonal: {", ".join([str(x) for x in main_diag])}. Sum: {sum(main_diag)}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diag])}. Sum: {sum(second_diag)}')