def generate_matrix(rows: int = 1, columns: int = 1) -> list[list[int]]:

    matrix: list = []

    for r in range(rows):
        matrix.append([])
        for c in range(columns):
            matrix[r].append([])
            matrix[r][c].append(0)

    return matrix

matrix = generate_matrix(2,2)

for row in matrix:
    print(row)