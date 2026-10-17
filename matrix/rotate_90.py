

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(matrix)
col = len(matrix[0])
result = [[0 for _ in range(row)] for _ in range(col)]

for i in range(0, row):
    for j in range(0, i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix [i][j]

for i in range(0, row):
    matrix[i].reverse()
